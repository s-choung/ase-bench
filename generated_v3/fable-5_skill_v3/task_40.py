from ase.spacegroup import crystal, get_spacegroup
from ase.io import read, write

nacl = crystal(['Na', 'Cl'], [(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

write('NaCl.cif', nacl)

atoms = read('NaCl.cif')
sg = get_spacegroup(atoms)

print(f"Spacegroup: {sg.symbol} (No. {sg.no})")
print(f"Number of atoms: {len(atoms)}")
print(f"Chemical formula: {atoms.get_chemical_formula()}")
