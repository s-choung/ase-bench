from ase import Atoms
from ase.calculators.emt import EMT
from ase.vegeometry import v0
from ase.neb import NEB
from ase.calculators.neb import NaturalCutoffs
from ase.calculators.neb import NaturalCutoffs

def interpolate_image_path(initial, final, number_of_images):
    """ Interpolates between two images"""
    images = [initial]
    for _ in range(number_of_images - 1):
        image = initial.copy()
        images.append(image)
    images.append(final)
    return images

# Create initial and final states
initial_image = Atoms(
    symbols='Al Al Al',
    positions=[[0, 0, 0], [0, 0, 0], [0, 0, 2]],  # two Al fixed
    cell=[2.842, 2.842, 2.842],
    pbc=[True] * 3
)

final_image = Atoms(
    symbols='Al Al Al',
    positions=[[0, 0, 0], [0, 0, 0], [0, 0, 3]],  # third Al is moved one unit along z-axis
    cell=[2.842, 2.842, 2.842],
    pbc=[True] * 3
)

# Assign the EMT calculator to all images
initial_image.set_calculator(EMT())
final_image.set_calculator(EMT())

# Interpolating the images
interpolated_images = interpolate_image_path(initial_image, final_image, number_of_images=3)

# Run NEB calculation and print energy of each image
neb = NEB(interpolated_images)
neb.interpolate(method='idpp')

for image in interpolated_images:
    image.set_calculator(EMT())  # ensure the EMT calculator is used
    image.run()  # compute energies
    energy = image.get_potential_energy()  # get energy of the image
    print(f"Energy of image: {energy} eV")

# Example output
