from ase.build import nanotube
from ase.io import write

# Create (6,6) carbon nanotube with length=4
cnt = nanotube(6, 6, length=4)

# Print number of atoms and cell info
print(f"Number of atoms: {len(cnt)}")
print("Cell info:")
print(f"  Cell vectors:\n{cnt.cell}")
print(f"  Periodic: {cnt.pbc}")

# Optional: Visualize structure (commented out)
# write('cnt.cif', cnt)
