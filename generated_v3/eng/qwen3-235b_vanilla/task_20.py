from ase import Atoms
from ase.visualize import view
from ase.geometry import carbon_nanotube

# Create a (6,6) carbon nanotube with length 4
cnt = carbon_nanotube(n=6, m=6, length=4)

# Print number of atoms and cell info
print("Number of atoms:", len(cnt))
print("Cell:", cnt.get_cell())
