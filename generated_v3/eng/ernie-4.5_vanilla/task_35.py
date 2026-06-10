from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize.bfgs import BFGS

# Create the initial and final states
start = Atoms('Al3', positions=[[0, 0, 0], [1, 0, 0], [0.5, 0.1, 0]])  # Initial state: third atom slightly off the line
finish = Atoms('Al3', positions=[[0, 0, 0], [1, 0, 0], [0.5, 1.0, 0]])  # Final state: third atom at the target position

# Fix the first two atoms in both configurations
for atoms in [start, finish]:
    atoms.set_constraint(FixedAtoms(indices=[0, 1]))  # Actually (in ASE you might use) a more common way is using:
    # Correction: Use explicit set_constraint method correctly via defining which atoms
from ase.constraints import FixAtoms
start.set_constraint(FixAtoms(mask=[i < 2 for i in range(3)]))  # Two first fixed
finish.set_constraint(FixAtoms(mask=[i < 2 for i in range(3)]))

# Set the EMT calculator
start.calc = EMT()
finish.calc = EMT()

# Create the NEB object with initial, final, and intermediate images
images = [start, None, None, finish]  # Three images: initial, two intermediates, and final
images = NEB(images, k=0.1)  # Simplified spring constant

# Perform interpolation of intermediate images
images.interpolate()

# Set the EMT calculator for intermediate images
for image in images.images[1:-1]:  # Skip first and last (they are already set)
    image.calc = EMT()

# Relax the NEB configuration
optimizer = BFGS(images, trajectory='neb_trajectory.traj')
optimizer.run(fmax=0.01)

# Print the energy of each image after relaxation
for i, image in enumerate(images.images):
    print(f"Image {i} energy: {image.get_potential_energy():.4f} eV")
