from ase.spacegroup import crystal
from ase.build import surface
import ase.io as io

# Create MoS2 monolayer crystal
a = 3.16  # Lattice parameter in angstroms
molecules_per_unit_cell = 2
mos2 = crystal(['Mo', 'S'],
               basis=[(0, 0, 0), (1/3, 1/3, 0.25)],  # Mo at (0,0,0) and S at (1/3,1/3,0.25) in fractional coordinates
               spacegroup=194,  # P-6m2 for MoS2
               cellparam=[a, a, 12.3, 90, 90, 120],  # cell parameters including a larger c-axis length to split layers
               primitive_cell=True)

# Generate a monolayer by slicing the bulk structure
mos2_monolayer = surface(mos2, indices=(1, 0, 0), layers=1, vacuum=10)

# Print cell size
print("Cell size (in angstroms):", mos2_monolayer.cell.cellpar())

# Optional: Save the structure to a file for visualization
io.write('mos2_monolayer.xyz', mos2_monolayer)
