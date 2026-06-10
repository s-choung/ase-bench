from ase import build, spacegroup
from ase.calculators.emt import EMT

# Create MoS2 monolayer (using spacegroup for bulk, slice to get monolayer)
bulk = spacegroup.crystal('MoS2', [(3.16, 3.16, 12.3), (90, 90, 120)], basis=[(1/3, 2/3, 0.25), (2/3, 1/3, 0.75)])
monolayer = build.cut(bulk, a=(1, 0, 0), b=(0, 1, 0), c=(0, 0, 1), nlayers=1)

# Add 10 angstroms of vacuum along the z-direction
monolayer.center(vacuum=10.0, axis=2)

# Use EMT calculator dummy for output purposes
monolayer.calc = EMT()
print("Cell size:", monolayer.get_cell_lengths_and_angles())
