from ase.build import fcc100
from ase.calculators.emt import EMT

# Create 3-layer Cu(100) slab with 3x3 in-plane repeats, 12Å vacuum
cu_slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)
cu_slab.calc = EMT()  # Assign ASE built-in EMT calculator

# Output required information
print(f"Number of atoms: {len(cu_slab)}")
print("\nUnit cell (Å):")
print(cu_slab.cell)
