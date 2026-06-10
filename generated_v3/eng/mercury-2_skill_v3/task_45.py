from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS
import numpy as np

def bond_len(atoms):
    return np.linalg.norm(atoms[0].position - atoms[1].position)

# H2 molecule
h2 = molecule('H2')
h2.calc = EMT()

print('Before constraint')
print('bond length =', bond_len(h2))
print('energy =', h2.get_potential_energy())

# set bond length to 0.9 Å
target = 0.9
vec = h2[1].position - h2[0].position
scale = target / np.linalg.norm(vec)
h2[1].position = h2[0].position + vec * scale

# fix the bond length
h2.set_constraint(FixBondLength(0, 1))

# relax (bond length stays fixed)
BFGS(h2).run(fmax=0.01, steps=100)

print('\nAfter constraint and relaxation')
print('bond length =', bond_len(h2))
print('energy =', h2.get_potential_energy())
