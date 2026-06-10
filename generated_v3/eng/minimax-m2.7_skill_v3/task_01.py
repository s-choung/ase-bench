from ase.build import bulk
from ase import Atoms

# Create Cu FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.615)

# Generate 2x2x2 supercell
supercell = cu_bulk * (2, 2, 2)

# Print cell info
cell = supercell.get_cell()
print("Cell vectors (Å):")
print(cell)
print("\nCell lengths and angles:")
lengths, angles = supercell.get_cell_lengths_and_angles()
print(f"  a, b, c = {lengths[:3]}")
print(f"  α, β, γ = {lengths[3:]}")

# Print number of atoms
print(f"\nNumber of atoms: {len(supercell)}")
