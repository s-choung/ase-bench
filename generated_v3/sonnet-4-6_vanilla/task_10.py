from ase.cluster import Octahedron
from ase.calculators.emt import EMT

atoms = Octahedron('Cu', length=5)
calc = EMT()
atoms.calc = calc

print(f"원자 수: {len(atoms)}")
print(f"positions shape: {atoms.positions.shape}")
