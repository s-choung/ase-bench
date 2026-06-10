from ase.build import bcc100

# Create the surface
surface = bcc100('Fe', size=(2, 2, 4), vacuum=10.0)

# Set the surface cell
surface.set_cell([a * 2 for a in [3.47, 3.47, 3.47]])

# Print the number of atoms and cell size
print(f"Number of atoms: {surface.num_atoms}")
print(f"Cell size: {surface.cell}")
