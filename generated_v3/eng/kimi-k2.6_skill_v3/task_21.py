from ase.cluster import Icosahedron

atoms = Icosahedron('Au', noshells=3)

print(f'Number of atoms: {len(atoms)}')
print(f'Center of mass: {atoms.get_center_of_mass()}')
