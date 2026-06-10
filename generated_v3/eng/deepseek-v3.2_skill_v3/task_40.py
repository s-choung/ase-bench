from ase.io import read, write
from ase.spacegroup import get_spacegroup

atoms = read('NaCl.cif')
write('NaCl_out.cif', atoms)

spg = get_spacegroup(atoms)
print(f'Spacegroup: {spg.symbol} ({spg.no})')
print(f'Number of atoms: {len(atoms)}')
