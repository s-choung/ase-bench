from ase.build import bulk, surface
from ase.visualize import view

# Create a bulk bcc iron crystal
bulk_fe = bulk('Fe', 'bcc', a=2.87, cubic=True)

# Create a (110) surface with specified parameters
fe_surface = surface(bulk_fe, (110), layers=4, size=(2, 2, 4), vacuum=10.0)

# Print the number of atoms
print(f"Number of atoms: {len(fe_surface)}")

# Print the cell size
print(f"Cell size: {fe_surface.cell}
