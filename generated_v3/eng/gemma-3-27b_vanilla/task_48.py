from ase.build import fcc111
from ase.calculators.emt import EMT

atoms = fcc111('Cu', size=(2, 2, 2), vacuum=1.0)
calc = EMT()
atoms.set_calculator(calc)
distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)
print(f"Minimum distance: {min(distances)}")
print(f"Maximum distance: {max(distances)}")
