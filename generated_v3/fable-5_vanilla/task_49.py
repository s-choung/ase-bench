import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# EOS로 격자상수 결정
volumes, energies = [], []
for a in np.linspace(3.5, 3.7, 9):
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (4 * v0) ** (1 / 3)
print(f'Optimized lattice constant: {a0:.4f} A')

# (111) slab 4층 생성
slab = fcc111('Cu', size=(2, 2, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

# 하부 2층 고정
tags = slab.get_tags()
slab.set_constraint(FixAtoms(mask=tags >= 3))

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.01)

print(f'Final energy: {slab.get_potential_energy():.6f} eV')
for layer in sorted(set(tags)):
    z_avg = slab.positions[tags == layer, 2].mean()
    print(f'Layer {layer}: avg z = {z_avg:.4f} A')
