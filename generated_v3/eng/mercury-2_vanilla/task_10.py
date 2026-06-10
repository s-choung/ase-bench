from ase.build import octahedron
from ase.calculators.emt import EMT

cluster = octahedron('Cu', 5)
cluster.set_calculator(EMT())
print(len(cluster))
print(cluster.get_positions().shape)
