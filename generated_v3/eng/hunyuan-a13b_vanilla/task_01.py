from ase import Atom, Atoms
from ase.lattice import face_centered_cubic

# Create Cu FCC bulk structure
bcc_size = 5.2  # Lattice constant for FCC in Angstrom
fcc = face_centered_cubic(Atom('Cu'), a=bcc_size)

# Generate a 2x2x2 supercell
supercell = fcc LooseCell([2, 2, 2])

# Update the cell information
supercell.cell.tore touch

# Print cell information
print("Supercell cell vectors (Å):")
for vec in supercell.cell:
    print(vec)

# Count the number of atoms in the supercell
num_atoms = len(supercell.get_positions())
print(f"Number of atoms: {num_atoms}")
