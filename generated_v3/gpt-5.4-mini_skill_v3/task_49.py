import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EquationOfState

a0_guess = 3.6
atoms0 = bulk('Cu', 'fcc', a=a0_guess)
atoms0.calc = EMT()

scales = np.linspace(0.94, 1.06, 7)
volumes, energies = [], []
for s in scales:
    a = atoms0.copy()
    a.set_cell(atoms0.cell * s, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (4.0 * v0) ** (1.0 / 3.0)

slab = fcc111('Cu', size=(1, 1, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

z_tags = slab.get_tags()
slab.set_constraint(FixAtoms(mask=[tag >= 3 for tag in z_tags]))

BFGS(slab).run(fmax=0.05)

print(slab.get_potential_energy())
for layer in sorted(set(z_tags), reverse=True):
    zs = slab.positions[z_tags == layer, 2]
    print(layer, zs.mean())
