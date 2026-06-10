from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Create initial and final states
initial = Atoms('Al3',
                positions=[[0, 0, 0], [1, 0, 0], [2, 0, 0]],
                calculator=EMT())
final = Atoms('Al3',
              positions=[[0, 0, 0], [1, 1, 0], [2, 0, 0]],
              calculator=EMT())

# Create initial images via linear interpolation
images = [initial]
for i in range(1, 3):
    images.append(initial.copy())
images.append(final)

# Linear interpolation for intermediate images
for i, image in enumerate(images):
    if 0 < i < 3:
        alpha = i / 3
        image.set_positions((1 - alpha) * initial.get_positions() +
                           alpha * final.get_positions())
    image.set_calculator(EMT())

# Fix the two end atoms (indices 0 and 2) in all images
constraint = FixAtoms(indices=[0, 2])
for image in images:
    image.set_constraint(constraint)

# Create and run NEB
neb = NEB(images, allow_shared_calculator=False)
optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

# Print energies of each image
print("\nImage energies:")
for i, image in enumerate(images):
    energy = image.get_potential_energy()
    print(f"Image {i}: {energy:.6f} eV")
