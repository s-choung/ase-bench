from ase.build import mx2
from ase import units

monolayer = mx2('MoS2', kind='2H', a=3.18, thickness=3.17)
monolayer.calc = None  # Clear any existing calculator
monolayer.cell[2, 2] += 10.0  # Add 10 Ångstroms of vacuum along z-axis
print(monolayer.get_cell_lengths_and_angles())
