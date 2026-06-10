from ase import Atoms
from ase.build import bulk, make_supercell

# Create a Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)

# Create a 2x2x2 supercell
supercell = make_supercell(atoms, (2, 2, 2))

# Print cell information
print("Cell parameters:")
print("a:", supercell.get_cell()[0])
print("b:", supercell.get_cell()[1])
print("c:", supercell.get_cell()[2])
print("alpha:", supercell.get_cell()[3])
print("beta:", supercell.get_cell()[4])
print("gamma:", supercell.get_cell()[5])

# Print the number of atoms
print("\nNumber of atoms:", len(supercell))
