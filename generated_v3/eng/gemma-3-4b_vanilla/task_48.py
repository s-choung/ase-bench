from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.geometry import get_distances
from ase.lattice.cubic import cubic_supercell

Cu = fcc111('Cu', size=(2, 2, 2), shiftme=False)
calc = EMT()
Cu.calc = calc
Cu.get_distances(mic=True)
distances = get_distances(Cu)
min_dist = min(distances)
max_dist = max(distances)
print(f"Minimum distance: {min_dist}")
print(f"Maximum distance: {max_dist}")
