from ase import Atoms
from ase.calculators.emt import EMT
import numpy as np

# Ti HCP parameters
a = 2.95
c_over_a = 1.59
c = a * c_over_a

# Lattice vectors for HCP
cell = np.array([
    [a, 0, 0],
    [-a/2, a*np.sqrt(3)/2, 0],
    [0, 0, c]
])

# Atomic positions for Ti in HCP (2 atoms per unit cell)
# Positions are fractional coordinates
positions = [
    [0, 0, 0],
    [1/3, 2/3, 1/2]
]

# Create the Atoms object
atoms = Atoms('Ti',
              scaled_positions=positions,
              cell=cell,
              pbc=True)

# Print cell vectors
print("Cell vectors:")
print(atoms.cell)
print("\nAtomic positions (Cartesian):")
print(atoms.get_positions())
