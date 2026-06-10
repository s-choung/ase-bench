from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
supercell = atoms * (2, 2, 2)

print(f"Cell lengths and angles: {supercell.get_cell_lengths_and_angles()}")
print(f"Number of atoms: {len(supercell)}")
