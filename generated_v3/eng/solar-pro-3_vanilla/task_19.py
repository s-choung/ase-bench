from ase import Atoms

# Create CO2 molecule: C at origin, O atoms at ±1.16 Å
atoms = Atoms('CO?',
             positions=[(0.0, 0.0, 0.0),
                       (1.16, 0.0, 0.0),
                       (-1.16, 0.0, 0.0)],
             pbc=False)
# Define a simple cubic cell (10 Å on each side)
atoms.set_cell([10.0, 10.0, 10.0], scale_atoms=True)

# Print all pairwise distances
for i in range(len(atoms)):
    for j in range(i+1, len(atoms)):
        d = atoms.get_distances(i, j)[0]
        print(f'{i}-{j}: {d:.3f} Å')
