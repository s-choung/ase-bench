from ase import Atoms

# Create Au FCC bulk
atoms = Atoms('Au', 'fcc', a=4.09, pbc=True, cell coordinates='fcc')

# Save to XYZ
Atoms.write('au_fcc.xyz', atoms, format='xyz')

# Read back
read_atoms = Atoms.read('au_fcc.xyz')

# Print info
print('Atom types:', read_atoms.get_atom_types())
print('Positions (Å):', read_atoms.get_positions(unit='angstrom'))
