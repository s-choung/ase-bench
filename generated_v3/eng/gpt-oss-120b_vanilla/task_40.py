from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# Create NaCl rock‑salt structure
nacl = bulk('NaCl', 'rocksalt', a=5.64)

# Save to CIF and read back
cif_path = 'NaCl.cif'
write(cif_path, nacl)
atoms = read(cif_path)

# Spacegroup info and atom count
sg = get_spacegroup(atoms, symprec=1e-2)
print('Spacegroup:', sg)
print('Number of atoms:', len(atoms))
