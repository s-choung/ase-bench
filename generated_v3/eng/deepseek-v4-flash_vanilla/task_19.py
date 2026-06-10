from ase import Atoms

# Create CO2 molecule: C at origin, O at ±1.16 Å along x-axis
positions = [
    [0.0, 0.0, 0.0],      # C
    [1.16, 0.0, 0.0],     # O1
    [-1.16, 0.0, 0.0]     # O2
]
atoms = Atoms('COO', positions=positions)
atoms.set_cell([10.0, 10.0, 10.0])
atoms.set_pbc(False)

# Calculate and print interatomic distances
distances = atoms.get_distances()
print("Interatomic distances (Å):")
print(distances)
