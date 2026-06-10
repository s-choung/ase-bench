from ase.spacegroup import crystal, get_spacegroup
from ase.io import read
from ase.calculators.emt import EMT

atoms = crystal('NaCl', basis=[(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, cellpar=5.69)
atoms.calc = EMT()
atoms.write('nacl.cif')

atoms_read = read('nacl.cif')
sg = get_spacegroup(atoms_read)

print(f"Spacegroup: {sg}")
print(f"Number of atoms: {len(atoms_read)}")
