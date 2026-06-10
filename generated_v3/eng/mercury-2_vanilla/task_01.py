from ase.build import bulk

# Cu FCC bulk, lattice constant ~3.6 Å
atoms = bulk('Cu', 'fcc', a=3.6)

# 2×2×2 supercell
atoms = atoms * (2, 2, 2)

print('Cell vectors (Å):')
print(atoms.get_cell())
print('Number of atoms:', len(atoms))
