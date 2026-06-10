from ase import Atoms
from ase.spacegroup import crystal

# Define the NaCl crystal structure with spacegroup 225 (Fm-3m)
# Lattice constant = 5.64 Å
# Na at (0, 0, 0) and Cl at (0.5, 0.5, 0.5)
NaCl = crystal(['Na', 'Cl'],
               cellpar=[5.64, 5.64, 5.64, 90, 90, 90],
               spacegroup=225,
               positions=[[0, 0, 0], [0.5, 0.5, 0.5]])

# Output the number of atoms and chemical symbols
print(f"Number of atoms: {len(NaCl)}")
print("Chemical symbols:", ' '.join(NaCl.symbols))
