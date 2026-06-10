from ase.spacegroup import crystal
from ase.io import write, read

atoms = crystal(['Na', 'Cl'], [(0,0,0), (0.5,0.5,0.5)], spacegroup=225, a=5.64)
write('NaCl.cif', atoms)
atoms_read = read('NaCl.cif')
sg = atoms_read.get_spacegroup()
print(f"Spacegroup: {sg.name} (no. {sg.number}), Atoms: {len(atoms_read)}")
