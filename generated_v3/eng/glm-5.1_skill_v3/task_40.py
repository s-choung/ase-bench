from ase.spacegroup import crystal
from ase.io import write, read

nacl = crystal(['Na', 'Cl'], [(0, 0, 0), (0.5, 0.5, 0)],
               spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

write('NaCl.cif', nacl, format='cif')
atoms = read('NaCl.cif')

print(f"Number of atoms: {len(atoms)}")
print(f"Space group: {atoms.info.get('spacegroup', 'N/A')}")
