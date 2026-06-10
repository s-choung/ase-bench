from ase.atoms import Atoms
from ase.cell import Cell
from ase.calculators.emt import EMT

# Create CO2 molecule
co2 = Atoms('C O O',
            positions=[[0.0, 0.0, 0.0],
                       [0.0, 1.16, 0.0],
                       [0.0, -1.16, 0.0]])

# Create a 10x10x10 cell with no pbc
cell = Cell(shape=(10, 10, 10))
co2.set_cell(cell, 'direct')
co2.pbc = False

# Set calculator
co2.calc = EMT()

# Calculate interatomic distances
distances = co2.get_distances()

# Print distances
print(distances)
