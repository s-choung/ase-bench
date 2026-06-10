"""T2 Wiki: Build FCC Cu bulk 2x2x2 supercell"""
from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
supercell = atoms * (2, 2, 2)
print(f"Number of atoms: {len(supercell)}")
print(f"Cell:\n{supercell.get_cell()}")
print(f"Volume: {supercell.get_volume():.2f} Å³")
