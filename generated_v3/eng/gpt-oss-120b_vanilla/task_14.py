from ase import Atoms
from ase.build import bulk

# NaCl rock‑salt structure, space group 225 (Fm‑3m)
a = 5.64  # Å
na_cl = bulk('NaCl', crystalstructure='rocksalt', a=a)

print('Number of atoms:', len(na_cl))
print('Chemical symbols:', na_cl.get_chemical_symbols())
