from ase.cluster.octahedron import Octahedron
from ase.build import bulk
from ase.calculators.emt import EMT

cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_bulk.calc = EMT()

cu_oct = Octahedron(cu_bulk, length=5)
num_atoms = len(cu_oct)
positions_shape = cu_oct.positions.shape

print(f'Number of atoms: {num_atoms}')
print(f'Positions shape: {positions_shape}')
