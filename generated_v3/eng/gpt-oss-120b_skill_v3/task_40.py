from ase.build import bulk
from ase.io import write, read

# Build NaCl rock‑salt structure
na_cl = bulk('NaCl', 'rocksalt', a=5.64)

# Save to CIF and read back
write('NaCl.cif', na_cl)
na_cl_read = read('NaCl.cif')

# Spacegroup info and atom count
sg = na_cl_read.get_spacegroup()
print(f'Spacegroup: {sg.symbol} (No. {sg.no})')
print('Number of atoms:', len(na_cl_read))
