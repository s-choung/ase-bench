from ase.build import bulk
from ase import Atoms

# Create Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.61)

# Generate 2x2x2 supercell
supercell = cu.repeat((2, 2, 2))

print("Cell:")
print(supercell.cell)
print("Number of atoms:", len(supercell))
