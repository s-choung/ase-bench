from ase.build import bulk
from ase.calculators import EMT

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

dist_list = atoms.get_distances(0, mic=True)

print(f"Min distance: {min(dist_list):.4f}")
print(f"Max distance: {max(dist_list):.4f}")
