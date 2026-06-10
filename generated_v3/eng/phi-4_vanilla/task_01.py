from ase.build import bulk, make_supercell
from ase import Atoms

# Create a Cu FCC bulk
cu_bulk = bulk('Cu', cubic=True, a=3.6)

# Generate a 2x2x2 supercell
supercell_matrix = (2, 2, 2)
cu_supercell = make_supercell(cu_bulk, supercell_matrix)

# Print the cell information
print("Cell Information:")
print(cu_supercell.get_cell())
print("Number of Atoms:", cu_supercell.get_global_number_of_atoms())
