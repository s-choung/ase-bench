from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
atoms.calc = EMT()

distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)
print(f"Minimum distance: {min(distances):.4f}")
print(f"Maximum distance: {max(distances):.4f}")
