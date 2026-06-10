from ase import Atoms
from ase.neb import NEB
from ase.calculators.emt import EMT

# Define initial and final positions for Al atoms
initial_positions = [(0, 0, 0), (3, 0, 0)]  # Fixed Al atoms positions
moving_position_start = (1.5, 0, 0)  # Start position of the third Al atom
moving_position_end = (1.5, 3, 0)  # End position of the third Al atom

# Create initial, midpoint, and final Atoms objects
initial = Atoms('Al3', positions=[initial_positions[0], initial_positions[1], moving_position_start])
middle = Atoms('Al3', positions=[(initial_positions[0][0] + moving_position_end[0] / 2, 0, 0), (3, 0, 0), (moving_position_end[0] / 2, 0, 0])
final = Atoms('Al3', positions=[initial_positions[0], initial_positions[1], moving_position_end])

# Initialize the EMT calculator for the initial state
initial.calc = EMT()
initial.set_calculator(initial.calc)

# Compute initial energy
initial.set_label('Initial')
initial.calculate()
initial_energy = initial.get_potential_energy()

# Initialize the EMT calculator for the final state
final.calc = EMT()
final.set_calculator(final.calc)

# Compute final energy
final.set_label('Final')
final.calculate()
final_energy = final.get_potential_energy()

# Perform NEB calculation
images = [initial, middle, final]
force = NEB(images=images, calculator=EMT(), interpolation={'Al3': 'LINEAR'})
images.interpolate_positions()
images.converge()
images.optimize_step()

# Print energies of all images
for image in images.images:
    image.set_calculator(EMT())
    image.calculate()
    print(f'Energy of {image.label}: {image.get_potential_energy()} eV')
