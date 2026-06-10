from ase import Atoms
from ase.geometry import get_distances

atoms = Atoms(
    symbols='OCO',
    positions=[[-1.16, 0.0, 0.0], [0.0, 0.0, 0.0], [1.16, 0.0, 0.0]],
    cell=[10.0, 10.0, 10.0],
    pbc=False
)

distances, _ = get_distances(atoms.positions, cell=atoms.cell, pbc=atoms.pbc)
print(distances)
