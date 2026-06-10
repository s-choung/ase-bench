from ase.build import mx2
from ase.calculators.emt import EMT
from ase import Atoms

# Create a MoS2 monolayer
mos2 = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10)

# Print the cell size
print(mos2.get_cell_lengths_and_angles())
