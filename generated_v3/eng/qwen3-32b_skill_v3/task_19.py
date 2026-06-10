from ase import Atoms
from ase.neighborlist import get_distances

atoms = Atoms(
    symbols=["C", "O", "O"],
    positions=[[0.0, 0.0, 0.0], [1.16, 0.0, 0.0], [-1.16, 0.0, 0.0]],
    cell=[10.0, 10.0, 10.0],
    pbc=False,
)

dists = get_distances(atoms.positions, cell=atoms.cell, pbc=atoms.pbc)["dists"]
print(f"C-O1: {dists[0][1]:.3f} Å")
print(f"C-O2: {dists[0][2]:.3f} Å")
print(f"O1-O2: {dists[1][2]:.3f} Å")
