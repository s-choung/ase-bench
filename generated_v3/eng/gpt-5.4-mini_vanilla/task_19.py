from ase import Atoms
from ase.geometry import get_distances

atoms = Atoms(
    symbols='CO2',
    positions=[(0.0, 0.0, 0.0), (1.16, 0.0, 0.0), (-1.16, 0.0, 0.0)],
    cell=[10.0, 10.0, 10.0],
    pbc=False
)

d = get_distances(atoms.positions[0], atoms.positions[1:], cell=atoms.cell, pbc=atoms.pbc)[1]
print("C-O distances:", d)
print("O-O distance:", get_distances(atoms.positions[1], atoms.positions[2], cell=atoms.cell, pbc=atoms.pbc)[1])
