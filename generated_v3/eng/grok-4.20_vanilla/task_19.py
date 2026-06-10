from ase import Atoms
import numpy as np

# Create CO2 molecule: C at origin, O at +/- 1.16 A along x-axis
atoms = Atoms('CO2',
              positions=[[0, 0, 0],
                         [1.16, 0, 0],
                         [-1.16, 0, 0]],
              cell=[10, 10, 10],
              pbc=False)

# Calculate and print interatomic distances
d = atoms.get_distances(0, [1, 2], mic=False)
print("C-O distances:", d)
d12 = atoms.get_distance(1, 2)
print("O-O distance:", d12)
