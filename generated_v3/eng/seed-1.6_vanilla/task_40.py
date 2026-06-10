from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup
from ase.calculators.emt import EMT

# Create NaCl bulk structure and assign built-in EMT calculator
nacl = bulk('NaCl', cubic=True)
nacl.calc = EMT()

# Save to CIF and read back
write('nacl.cif', nacl)
nacl_read = read('nacl.cif')

# Get and print spacegroup and atom count
sg = get_spacegroup(nacl_read)
print(f'Spacegroup: {sg}')
print(f'Number of atoms: {len(nacl_read)}')
