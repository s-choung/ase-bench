from ase.cluster import Icosahedron
from ase.calculators.emt import EMT

# Initialize 3-shell gold icosahedron nanoparticle
au_np = Icosahedron('Au', noshells=3)
au_np.calc = EMT()

# Print required properties
print(f"Number of atoms: {len(au_np)}")
print(f"Center of mass (Å): {au_np.get_center_of_mass()}")
