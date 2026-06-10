from ase.cluster.octahedron import Octahedron
from ase.calculators.emt import EMT

# Build Cu octahedron nanoparticle, length=5 means 5 layers from center to facet
atoms = Octahedron('Cu', length=5)

# Assign EMT calculator (optional step, demonstrates calculating energy)
atoms.calc = EMT()
atoms.get_potential_energy()

# Print number of atoms and positions shape
print(len(atoms))
print(atoms.positions.shape)
