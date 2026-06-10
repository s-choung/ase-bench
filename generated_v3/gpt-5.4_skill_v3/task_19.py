from ase import Atoms
from ase.geometry import get_distances

atoms = Atoms(
    symbols='OCO',
    positions=[(-1.16, 0.0, 0.0), (0.0, 0.0, 0.0), (1.16, 0.0, 0.0)],
    cell=(10.0, 10.0, 10.0),
    pbc=False,
)

d01 = get_distances(atoms.positions[0], atoms.positions[1])[1][0, 0]
d12 = get_distances(atoms.positions[1], atoms.positions[2])[1][0, 0]
d02 = get_distances(atoms.positions[0], atoms.positions[2])[1][0, 0]

print('O(0)-C(1):', d01)
print('C(1)-O(2):', d12)
print('O(0)-O(2):', d02)
