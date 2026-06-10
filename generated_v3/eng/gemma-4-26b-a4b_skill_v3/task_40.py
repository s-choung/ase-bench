from ase.build import bulk
from ase.io import write, read

# Create NaCl (fcc structure with two atoms in basis)
# NaCl is typically described by an fcc lattice of Cl- with Na+ in octahedral sites
atoms = bulk('NaCl', 'rocksalt', a=5.64)

# Save to CIF format
write('nacl.cif', atoms)

# Read it back
read_atoms = read('nacl.cif')

# Print spacegroup and number of atoms
# Note: spacegroup is retrieved from the atoms object via the symmetry module
from ase.spacegroup import crystal
print(f"Spacegroup: {read_atoms.get_spacegroup()}")
print(f"Number of atoms: {len(read_atoms)}")
