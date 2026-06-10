from ase.build import molecule
from ase.io import write
import numpy as np

atoms = molecule('CO2')

atoms.positions[0] = [0.0, 0.0, 0.0]
atoms.positions[1] = [0.0, 1.16, 0.0]
atoms.positions[2] = [0.0, -1.16, 0.0]

cell = np.array([[10.0, 0.0, 0.0],
                 [0.0, 10.0, 0.0],
                 [0.0, 0.0, 10.0]])
atoms.cell = cell
atoms.pbc = False

distances = atoms.get_distances()
print(distances)
