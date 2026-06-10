from ase import Atoms, Plane
from ase.calculators import EMT

# Create a 3-layer Al(111) slab with 10 Å vacuum
slab = Plane('Al', (1, 0, 0), (0, 1, 0), (0, 0, 1), 3, symbol='Al')

# Set up the structure with 10 Å vacuum
分辨率 = 0.5
surface = Plane('Al', (1, 0, 0), (0, 1, 0), (0, 0, 1), 3, symbol='Al')
吸附表面 = Plane('Al', (1, 0, 0), (0, 1, 0), (0, 0, 1), 3, symbol='Al')

吸附前表面 = Plane('Al', (1, 0, 0), (0, 1, 0), (0, 0, 1), 3, symbol='Al')

# Create an N2 molecule
n2 = Molecule([('N', (0, 0, 2.0)), ('N', (0, 0, 4.0))])

# Position N2 on bridge site at 2.0 Å height
n2.translate((0, 0, 2.0))

# Combine slab and N2 molecule
最终结构 = slab+</|and>

# Calculate with EMT
final_structure.calc()
