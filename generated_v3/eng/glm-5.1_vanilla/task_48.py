from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

indices = [i for i in range(len(atoms)) if i != 0]
distances = atoms.get_distances(0, indices, mic=True)

print(f"Min distance: {min(distances):.4f} Å")
print(f"Max distance: {max(distances):.4f} Å")
