import numpy as np
from ase import Atoms
from ase.build import fcc111, molecule
from ase.calculators.emt import EMT
from ase.calculators.neb import NEB
from ase.dft.bardep import bardep
from ase.neighborlist import NeighborList
from ase.md.langevin import Langevin
from ase.visualize import view
from ase.spacegroup import crystal

# Define the initial and final states
initial_state = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
final_state = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
final_state.add_atom(1, (0.866, 0.0, 0.0))  # hcp hollow site

# Create the adatom
adatom = molecule('Cu')

# Build the initial surface
initial_state.calc = EMT()
initial_state.set_cell(initial_state.get_cell())

# Add the adatom to the initial surface
adatom.center = initial_state.positions[0]
initial_state.add_atom(1, adatom.positions)

# Set up the NEB calculation
images = [initial_state.copy()] + [initial_state.copy() for _ in range(4)] + [final_state.copy()]
neb = NEB(images)
neb.interpolate(method='idpp')
for img in images[1:-1]: img.calc = EMT()

# Perform the NEB calculation
neb.run(fmax=0.02)

# Extract the energy barrier
max_energy = np.max([img.get_potential_energy() for img in images[1:-1]])
initial_energy = initial_state.get_potential_energy()
energy_barrier = max_energy - initial_energy

# Print the energy barrier
print(f"Energy barrier: {energy_barrier:.4f} eV")

# Visualize the trajectory (optional)
view(initial_state)
