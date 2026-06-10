"""T2 Skill: Build FCC Cu bulk 2x2x2 supercell"""
from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6)
supercell = atoms.repeat((2, 2, 2))
print(f"Number of atoms: {len(supercell)}")
print(f"Cell:\n{supercell.get_cell()}")
