from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB

# Define initial, final, and intermediate images
initial = Atoms('Al', positions=[[0, 0, 0]])
final = Atoms('Al', positions=[[3, 0, 0]])
images = [initial.copy(), Atoms('Al', positions=[[1, 0, 0]]), final.copy()]

# Linearly interpolate positions between initial and final
images[1].set_positions((1 / 3) * initial.positions + (2 / 3) * final.positions)

# Set up EMT calculator for all images
for image in images:
    image.set_calculator(EMT())

# Perform NEB calculation
neb = NEB(images)
neb.interpolate()

# Calculate and print the energy of each image
for i, image in enumerate(images):
    energy = image.get_potential_energy()
    print(f"Image {i}: Energy = {energy} eV")
