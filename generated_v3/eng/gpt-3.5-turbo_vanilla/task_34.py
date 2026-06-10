from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

# Define initial and final states
initial = Atoms('Cu',
                 positions=[[0, 0, 0]],
                 calculator=EMT())
final = Atoms('Cu',
               positions=[[0.5, 0.5, 0]],
               calculator=EMT())

# Images with IDPP interpolation
images = [initial] + [Atoms('Cu', calculator=EMT()) for i in range(3)] + [final]

# Set up NEB calculation
neb = NEB(images, k=0.1)

# Optimize the NEB path
optimizer = BFGS(neb)
optimizer.run(fmax=0.05)

# Calculate energy barrier
initial_energy = images[0].get_potential_energy()
max_energy = max(image.get_potential_energy() for image in images)

# Print energy barrier
print("Energy barrier:", max_energy - initial_energy)
