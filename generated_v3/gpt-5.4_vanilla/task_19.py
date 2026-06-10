from ase import Atoms

d = 1.16
atoms = Atoms(
    symbols=['O', 'C', 'O'],
    positions=[[-d, 0, 0], [0, 0, 0], [d, 0, 0]],
    cell=[10, 10, 10],
    pbc=False
)

dists = atoms.get_distances(1, [0, 2], mic=False)
print("C-O distances:", dists)
print("O-O distance:", atoms.get_distances(0, [2], mic=False)[0])
