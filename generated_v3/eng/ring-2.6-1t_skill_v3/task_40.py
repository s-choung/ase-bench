from ase.spacegroup import crystal, get_spacegroup
from ase.io import write, read

# Create NaCl (rock-salt, Fm-3m, No. 225)
nacl = crystal(['Na', 'Cl'],
               basis=[[0, 0, 0], [0.5, 0, 0]],
               spacegroup=225,
               cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

# Save CIF
write('NaCl.cif', nacl, format='cif')

# Read back
atoms = read('NaCl.cif')

sg = get_spacegroup(atoms)
print(f'Spacegroup: {sg}')
print(f'Number of atoms: {len(atoms)}')
