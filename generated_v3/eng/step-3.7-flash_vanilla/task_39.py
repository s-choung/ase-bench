from ase import build, io

au_bulk = build.bulk('Au', 'fcc', a=4.08)
io.write('au_fcc_bulk.xyz', au_bulk)
au_read = io.read('au_fcc_bulk.xyz')
print("Atom types:", au_read.get_chemical_symbols())
print("Positions (Å):\n", au_read.get_positions())
