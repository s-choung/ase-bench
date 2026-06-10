from ase.build import bulk
from ase.calculators.emt import EMT

cu = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
distances = cu.get_distances(0, range(len(cu)), mic=True)
print(f"Minimum distance: {min(distances):.3f} Å")
print(f"Maximum distance: {max(distances):.3f} Å")
