from ase.cluster import Icosahedron

# Create 3-shell gold icosahedron nanoparticle
au_icosahedron = Icosahedron('Au', noshells=3)

# Print required properties
print(f"Number of atoms: {len(au_icosahedron)}")
center_of_mass = au_icosahedron.get_center_of_mass()
print(f"Center of mass (Å): {center_of_mass.round(3)}")
