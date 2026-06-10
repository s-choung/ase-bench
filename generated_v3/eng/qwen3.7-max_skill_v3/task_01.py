from ase.build import bulk

atoms = bulk('Cu', 'fcc')
supercell = atoms * (2, 2, 2)

print(f"Cell:\n{supercell.cell[:]}")
print(f"Lengths and angles: {supercell.get_cell_lengths_and_angles()}")
print(f"Number of atoms: {len(supercell)}")
