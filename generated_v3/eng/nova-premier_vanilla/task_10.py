from ase.cluster.octahedron import Octahedron
from ase.calculators.emt import EMT

atoms = Octahedron('Cu', 5, 2, cutoff=1.2)
atoms.calc = EMT()
print(f"Number of atoms: {len(atoms)}")
print(f"Positions shape: {atoms.positions.shape}")
