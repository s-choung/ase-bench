from ase.cluster import Octahedron
from ase.data import reference_states, atomic_numbers

a = reference_states[atomic_numbers['Cu']]['a']
atoms = Octahedron('Cu', length=5, latticeconstant=a)

print(f"Number of atoms: {len(atoms)}")
print(f"Positions shape: {atoms.positions.shape}")
