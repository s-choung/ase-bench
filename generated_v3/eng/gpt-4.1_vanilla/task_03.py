from ase.build import mx2
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT

# Create MoS2 monolayer, periodic in-plane (3x3 cell for realism)
slab = mx2('MoS2', '2H', a=3.18, thickness=1, size=(1, 1, 1), vacuum=10.0)

# Optionally, assign a calculator, though not strictly needed for cell output
slab.calc = EMT()

print('Cell size (Angstrom):')
print(slab.cell.lengths())
