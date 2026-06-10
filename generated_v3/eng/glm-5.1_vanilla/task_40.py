from ase.build import bulk
from ase.io import read, write
from ase.spacegroup import get_spacegroup
from ase.calculators.emt import EMT

atoms = bulk('NaCl', 'rocksalt', a=5.64)
atoms.calc = EMT()

write('NaCl.cif', atoms)
atoms_read = read('NaCl.cif')

print(f"Spacegroup: {get_spacegroup(atoms_read)}")
print(f"Number of atoms: {len(atoms_read)}")
