from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS
import numpy as np

def bond_len(atoms):
    return np.linalg.norm(atoms[0].position - atoms[1].position)

# H2 molecule
h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])  # Å
h2.set_calculator(EMT())

# before constraint
e0 = h2.get_potential_energy()
d0 = bond_len(h2)
print(f'Before: bond length = {d0:.3f} Å, energy = {e0:.5f} eV')

# apply constraint (0.9 Å) and relax
h2.set_constraint(FixBondLength(0, 1, 0.9))
opt = BFGS(h2, logfile=None)
opt.run(fmax=0.01, steps=100)

# after constraint
e1 = h2.get_potential_energy()
d1 = bond_len(h2)
print(f'After:  bond length = {d1:.3f} Å, energy = {e1:.5f} eV')
