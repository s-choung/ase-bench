from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.08)
write('Au_fcc.xyz', atoms)
loaded_atoms = read('Au_fcc.xyz')

print('Symbols:', loaded_atoms.get_chemical_symbols())
print('Positions:')
for i, pos in enumerate(loaded_atoms.get_positions()):
    print(f'  {i}: {pos}')
