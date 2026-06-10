from ase.spacegroup import crystal, get_spacegroup
from ase.io import write, read

atoms = crystal(['Na', 'Cl'], [(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])
write('nacl.cif', atoms)
atoms = read('nacl.cif')
sg = get_spacegroup(atoms)
print(f"{sg.symbol} ({sg.no})")
print(len(atoms))
