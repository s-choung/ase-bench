from ase.build import mx2
from ase.io import write

# Create MoS2 monolayer (2H phase)
mo2s = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10.0)

# Print cell dimensions
cell_params = mo2s.get_cell_lengths_and_angles()
print(f"Cell size: a={cell_params[0]:.2f} Å, b={cell_params[1]:.2f} Å, c={cell_params[2]:.2f} Å")
