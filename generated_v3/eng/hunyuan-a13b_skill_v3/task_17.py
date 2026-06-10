from ase.build import bulk, surface, add_vacuum

# Create Cu bulk
Cu_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)

# Cut (2,1,1) surface with 3 layers
Cu_surface = surface('fcc', (2, 1, 1), layers=3)

# Add 10 Å vacuum in z-direction
Cu_surface_with_vacuum = add_vacuum(Cu_surface, 10.0)

# Get number of atoms and cell dimensions
num_atoms = len(Cu_surface_with_vacuum)
cellLengths = Cu_surface_with_vacuum.get_cell_lengths_and_angles()[:3]

print(f"Number of atoms: {num_atoms}")
print(f"Cell lengths (Å): {cellLengths}")
