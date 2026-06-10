from ase.cluster import Icosahedron

# Create Au Icosahedron nanoparticle
# Note: 'noshells' is not a standard parameter in Icosahedron; 
# 'length' (number of shells) is used to control size.
atoms = Icosahedron('Au', length=3)

# Output results
print(f"Number of atoms: {len(atoms)}")
print(f"Center of mass: {atoms.get_center_of_mass()}")
