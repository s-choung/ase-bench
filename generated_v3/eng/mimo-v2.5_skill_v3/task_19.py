from ase import Atoms
from ase.geometry import get_distances

# CO2: O=C=O, bond length 1.16 Å
atoms = Atoms(
    symbols='CO2',
    positions=[[0, 0, 0],       # C
               [0, 0, 1.16],     # O (right)
               [0, 0, -1.16]],   # O (left)
    cell=[10, 10, 10],
    pbc=False
)

distances = get_distances(atoms)
print("Interatomic distances (Å):")
print(distances[1])  # distance matrix
print(f"\nC-O bond length: {distances[1][0,1]:.2f} Å")
print(f"O-O distance:    {distances[1][1,2]:.2f} Å")
