from ase.build import mx2  # Build the MoS2 monolayer
from ase.build import add_2d_material  # Add vacuum in the z-direction

# Create MoS2 monolayer
layer = mx2('MoS2', size=(1, 1, 1), thickness=2, layers='mo', \
          layer_spacing=0.000, kind='2H', a=3.16)  # Creates a MoS2 layer with specified parameters

# Add vacuum along the z-direction for 2D material
layer = add_2d_material(layer, vacuum=10.0, space_fill=True)  # Adds 10 angstroms of vacuum

# Print cell size before and after adding the vacuum
import numpy as np
initial_cell = layer.get_cell()
print("Original Cell Size: ", initial_cell.diagonal())
final_cell = layer.get_cell()
print("Modified Cell Size with Vacuum: ", final_cell.diagonal())
