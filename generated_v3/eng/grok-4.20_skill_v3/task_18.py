from ase.build import molecule
from ase.geometry import get_distances
import numpy as np

atoms = molecule('CH4')
print(atoms.get_chemical_formula())
print('Coordinates:')
print(atoms.get_positions())

d = get_distances([0], range(1,5), positions=atoms.positions)[0][0]
print('C-H bond lengths:', np.round(d, 6))
