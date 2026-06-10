from ase import Atoms

# Create CO2 molecule: C at (0,0,0), O at (±1.16, 0, 0)
atoms = Atoms('CO2',
              positions=[(0.0, 0.0, 0.0),
                         (1.16, 0.0, 0.0),
                         (-1.16, 0.0, 0.0)])

# Set cell to 10 Å cube, no periodic boundary conditions
atoms.set_cell([10.0, 10.0, 10.0])
atoms.set_pbc(False)

# Calculate and print all pairwise distances
distances = atoms.get_distances(mic=False)  # mic=False for no minimum image
print("Interatomic distances (Å):")
print(distances)
