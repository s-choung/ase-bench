from ase.build import fcc111, add_adsorbate
from ase.calculators import EMT
from ase.constraints import FixAtoms
from ase.io import write
import numpy as np

# Build a simple Al(111) surface
surface = fcc111('Al', size=(3, 3, 3))

# Add two fixed Al atoms
add_adsorbate(surface, 'Al', height=2.0, position=(0, 0.5, 0))
add_adsorbate(surface, 'Al', height=2.0, position=(1, 0.5, 0))

# Create atoms for the moving Al atom
moving_atom = [atom for atom in surface if atom.symbol == 'Al'][2]
initial_state = surface.copy()
final_state = surface.copy()
moving_atom.position[:] = (1.5, 0.5, 0)
final_state[2].position[:] = (1.5, 0.5, 0)

# Define the images
images = []
for i in np.linspace(0, 1, 3):
    images.append(initial_state.copy())
    moving_atom.position[:] = (i * 1.5 + (1 - i) * 1.5, 0.5, 0)
    images.append(final_state.copy())

# Create the ASE calculation object
calc = EMT()
surface.calc = calc

# Apply a constraint to fix the initial atoms
constraint = FixAtoms(indices=[0, 1])
surface.set_constraint(constraint)

# Perform the NEB calculation for each image
for i, image in enumerate(images):
    calc.setbox(image.get_cell())
    energy = image.get_potential_energy()
    print(f"Image {i+1}: Energy = {energy}")
    write(f"image_{i+1}.xyz", image)
