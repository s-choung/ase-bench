from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

# Define lattice parameter for Al (fcc)
a = 4.05

# Create initial and final Al dimer with a third atom moving
initial = Atoms('Al2', positions=[[0, 0, 0], [0.5, 0.5, 0.5]], cell=[a, a, a], pbc=True)
initial.add_atom(atoms=[0.25, 0.25, 0.25])  # third Al atom in the center

final = Atoms('Al2', positions=[[0, 0, 0], [0.5, 0.5, 0.5]], cell=[a, a, a], pbc=True)
final.positions[2] = [0.5, 0.5, 0.5]  # move third Al to one of the original positions

# Set EMT calculator for all atoms
initial.calc = EMT()
final.calc = EMT()

# Linearly interpolate to create 3 images (including initial and final)
images = [initial] + [initial.copy() for _ in range(1)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

# Optimize the intermediate image
if len(images) > 2:
    neb[1].calc = EMT()  # only the intermediate image needs a calculator
    opt = BFGS(neb)
    opt.run(fmax=0.05)

# Print energies of each image
for i, image in enumerate(images):
    image.calc = EMT() if i != 1 else None  # recompute energies for all except intermediate (already optimized)
    energy = image.get_potential_energy()
    print(f'Image {i}: Energy = {energy:.6f} eV')
