from ase import Atoms
from ase.build import bulk, make_supercell
from ase.io import write

# Create Cu FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.61)

# Generate 2x2x2 supercell
supercell = make_supercell(cu_bulk, [[2,0,0],[0,2,0],[0,0,2]])

# Print cell info and number of atoms
cell_params = supercell.get_cell_lengths_and_angles()
print(f"Cell parameters: a={cell_params[0]:.3f}, b={cell_params[1]:.3f}, c={cell_params[2]:.3f}")
print(f"Angles: α={cell_params[3]:.1f}°, β={cell_params[4]:.1f}°, γ={cell_params[5]:.1f}°")
print(f"Number of atoms: {len(supercell)}")
