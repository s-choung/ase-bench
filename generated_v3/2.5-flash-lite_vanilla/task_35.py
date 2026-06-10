from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import QuasiNewton
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase import Atoms

# Initial and final configurations
initial_atoms = Atoms('Al3', positions=[(0, 0, 0), (2.86, 0, 0), (1.43, 2.47, 0)], pbc=True)
final_atoms = Atoms('Al3', positions=[(0, 0, 0), (1.43, 2.47, 0), (2.86, 0, 0)], pbc=True)

# Set up NEB
images = [initial_atoms]
for _ in range(3):
    images.append(initial_atoms.copy())
images.append(final_atoms)

neb = NEB(images)
neb.interpolate(mic=True)

# Set calculators for each image
for image in images:
    image.calc = EMT()

# Optimize images
optimizer = QuasiNewton(neb, trajectory='neb.traj')
optimizer.run()

# Print energies of each image
for i, image in enumerate(images):
    energy = image.get_potential_energy()
    print(f"Image {i}: Energy = {energy:.4f} eV")
