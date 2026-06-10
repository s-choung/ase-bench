from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# FCC(111) slab 생성
slab = fcc111('Cu', size=(4, 4, 4), vacuum=10.0)
slab.set_constraint(FixAtoms(mask=[a.tag >= 2 for a in slab]))

# Initial: fcc hollow
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=2.5, position='fcc')

# Final: hcp hollow (약간 다른 위치)
final = slab.copy()
add_adsorbate(final, 'Cu', height=2.5, position='hcp')

# NEB 이미지 생성 (5개 중간 이미지)
images = [initial] + [initial.copy() for _ in range(5)] + [final]

# IDPP interpolation
neb = NEB(images)
neb.interpolate(method='idpp')

# Calculator 설정 (중간 이미지만)
for img in images[1:-1]:
    img.calc = EMT()

# NEB 최적화
dyn = BFGS(neb, trajectory='neb.traj')
dyn.run(fmax=0.05)

# 에너지 계산
initial.calc = EMT()
final.calc = EMT()

energies = []
for img in images:
    img.calc = EMT()
    energies.append(img.get_potential_energy())

energies = np.array(energies)
barrier = np.max(energies) - energies[0]

print(f"Initial energy: {energies[0]:.4f} eV")
print(f"Final energy: {energies[-1]:.4f} eV")
print(f"Maximum energy: {np.max(energies):.4f} eV")
print(f"Energy barrier: {barrier:.4f} eV")
print(f"\nEnergies along path:")
for i, e in enumerate(energies):
    print(f"  Image {i}: {e:.4f} eV")
