from ase import Crystal
from ase.io import write, read_cif

atoms = Crystal(symbols=['Na', 'Cl'], basis=[[0, 0, 0], [0.5, 0.5, 0.5]], a=5.64)
write('NaCl.cif', atoms)
atoms2 = read_cif('NaCl.cif')
sg = atoms2.get_spacegroup()
print(f"Spacegroup: {sg[0]} ({sg[1]})")
print(f"Number of atoms: {len(atoms2)}")
