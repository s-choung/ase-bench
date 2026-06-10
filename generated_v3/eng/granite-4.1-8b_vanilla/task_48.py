from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk

# Create a Cu FCC bulk structure, 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.61) * 2

# Assign a calculator (EMT) and perform a single energy calculation to build the structure
atoms.calc = EMT()
atoms.get_potential_energy()

# Get distances from atom 0 to all other atoms with mic=True for periodic boundary conditions
distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)

# Print minimum and maximum distances
print("Min distance:", min(distances))
print("Max distance:", max(distances))
