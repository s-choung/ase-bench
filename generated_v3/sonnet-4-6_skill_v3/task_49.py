import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# EOS로 격자상수 결정
atoms0 = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms0.calc = EMT()
cell0 = atoms0.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 11):
    a = atoms0.copy()
    a.set_cell(cell0 * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_opt = (v0 / 4) ** (1/3) * 4 ** (1/3)  # fcc: 4 atoms/cell, V = a^3/4 * 4
# 더 직접적으로: a = (4 * v0 / 4)^(1/3) = v0^(1/3)
a_opt = v0 ** (1/3)
print(f"EOS 최적 격자상수: {a_opt:.4f} Å")
print(f"EOS 최소 에너지: {e0:.4f} eV")
print(f"Bulk modulus: {B/units_kJ:.2f} GPa" if False else f"Bulk modulus: {B:.4f} eV/Å³")

# 올바른 격자상수 계산: cubic bulk는 4 atoms, V_cell = a^3
# atoms0 cubic=True → 4 atoms, V = a^3 → a = V^(1/3)
a_opt = v0 ** (1/3)
print(f"격자상수 (재확인): {a_opt:.4f} Å")

# (111) slab 4층 생성
slab = fcc111('Cu', size=(2, 2, 4), a=a_opt, vacuum=10.0)
slab.calc = EMT()

# 하부 2층 고정 (tag 기준: fcc111은 하부가 높은 tag)
tags = slab.get_tags()
print(f"Tags: {np.unique(tags)}")
# fcc111: tag=1이 최하층, tag=4가 최상층
constraint = FixAtoms(mask=[t <= 2 for t in tags])
slab.set_constraint(constraint)

# BFGS relaxation
opt = BFGS(slab, trajectory='slab_relax.traj')
opt.run(fmax=0.05)

# 결과 출력
energy = slab.get_potential_energy()
print(f"\n최종 에너지: {energy:.4f} eV")

positions = slab.get_positions()
tags = slab.get_tags()
print("\nLayer별 평균 z 좌표:")
for layer in sorted(np.unique(tags)):
    mask = tags == layer
    z_mean = positions[mask, 2].mean()
    print(f"  Layer {layer} (tag={layer}): z_mean = {z_mean:.4f} Å")
