from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

other = list(range(1, len(atoms)))
d = atoms.get_distances(0, other, mic=True)

print(f"Min: {d.min():.4f}")
print(f"Max: {d.max():.4f}")
