from ase import Atoms
from ase.calculators.emt import EMT
from ase.io import write

# Create CO2 molecule
c = Atoms('C', positions=[(0, 0, 0)])
o1 = Atoms('O', positions=[(1.16, 0, 0)])
o2 = Atoms('O', positions=[(-1.16, 0, 0)])
co2 = c + o1 + o2

# Set the cell and periodic boundaries
co2.set_cell((10, 10, 10))
co2.set_pbc(False)

# Calculate and print interatomic distances
distances = co2.get_distances(0, [1, 2], mic=False)
print("C-O distances (Å):", distances)
