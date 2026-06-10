from ase import Atoms

# CO2: C at origin, O at ±1.16 Å along x
atoms = Atoms(
    symbols=['C', 'O', 'O'],
    positions=[(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)],
    cell=[10, 10, 10],
    pbc=False,
)

# interatomic distance matrix (Å)
distances = atoms.get_all_distances(mic=False)
print(distances)
