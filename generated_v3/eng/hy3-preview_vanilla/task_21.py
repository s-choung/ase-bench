from ase.cluster import icosahedron
from ase.calculators.emt import EMT

atoms = icosahedron('Au', noshells=3)
atoms.calc = EMT()

print(f"Number of atoms: {len(atoms)}")
print(f"Center of mass: {atoms.get_center_of_mass()}")
