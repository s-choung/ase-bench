from ase.cluster import Icosahedron

au_icosa = Icosahedron('Au', noshells=3)
print(f'Number of atoms: {len(au_icosa)}')
print(f'Center of mass: {au_icosa.get_center_of_mass()}')
