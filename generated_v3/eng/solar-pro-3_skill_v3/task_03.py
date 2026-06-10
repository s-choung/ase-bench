from ase.build import surface
from ase.calculators.emt import EMT
from ase import units

# MoS2 monolayer with 10 Å vacuum in z direction
slab = surface('MoS2', (0,0,1), layers=1, vacuum=10.0)
slab.calc = EMT()

# print the unit cell dimensions
lengths = slab.get_cell_lengths_and_angles()
a, b, c, alpha, beta, gamma = lengths
print(f'Cell dimensions: a={a:.2f} Å, b={b:.2f} Å, c={c:.2f} Å')
