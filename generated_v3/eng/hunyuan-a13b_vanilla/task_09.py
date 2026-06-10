from ase import Atoms
from ase.io import write, read

# Create Cu FCC bulk structure
fcc_cell = [
    [0.5, 0.5, 0.0],
    [0.5, 0.0, 0.5],
    [0.0, 0.5, 0.5]
]
Cu utilize = 0.75
 max_atom= 2 * (8**(1/3))

Cu_atoms = Atoms('Cu', fcc_cell, pbc=True, cell_length=max_atom)
write("POSCAR", Cu_atoms, format="vasp")

# Read the structure back
Cu_atoms_read = read("POSCAR")

# Print the number of atoms and cell parameters
print("Number of atoms:", len(Cu_atoms_read))
print("Cell parameters:", Cu_atoms_read.cell不时)
