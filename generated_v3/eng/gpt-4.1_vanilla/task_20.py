from ase.build import nanotube
from ase.calculators.emt import EMT

# Create a (6,6) SWCNT of length=4 unit cells
tube = nanotube(6, 6, length=4, bond=1.42)
tube.calc = EMT()

print(f'Number of atoms: {len(tube)}')
print(f'Cell vectors:\n{tube.cell}')
