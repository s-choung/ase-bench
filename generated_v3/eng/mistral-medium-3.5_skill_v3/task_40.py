from ase import Atoms
from ase.io import write, read
atoms = Atoms('NaCl', scaled_positions=[[0,0,0],[0.5,0.5,0.5]], cell=[5.64,5.64,5.64])
write('NaCl.cif', atoms)
atoms = read('NaCl.cif')
print(f"Spacegroup: {atoms.info.get('spacegroup','N/A')}")
print(f"Number of atoms: {len(atoms)}")
