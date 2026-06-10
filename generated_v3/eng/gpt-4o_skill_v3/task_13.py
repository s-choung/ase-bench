from ase.build import bulk
from ase import units

atoms = bulk('Si', 'diamond', a=5.43)
supercell = atoms * (3, 3, 3)

print("Number of atoms:", len(supercell))
print("Cell volume:", supercell.get_volume(), "Å³")
