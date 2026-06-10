from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import FIRE

# Fixed atoms positions
fixed_pos = [(0.0, 0.0, 0.0), (5.0, 0.0, 0.0)]

# Initial state: moving atom near first fixed atom
initial = Atoms('Al3', positions=[fixed_pos[0], (1.0, 0.0, 0.0), fixed_pos[1]])
initial.set_calculator(EMT())
initial.set_constraint([True, False, True])  # Fix first and last atom

# Final state: moving atom near second fixed atom
final = Atoms('Al3', positions=[fixed_pos[0], (4.0, 0.0, 0.0), fixed_pos[1]])
final.set_calculator(EMT())
final.set_constraint([True, False, True])

# Create 3 images (initial, intermediate, final) via linear interpolation
images = [initial]
images += [initial.copy() for _ in range(1)]  # 1 intermediate image
images.append(final)

neb = NEB(images)
neb.interpolate()

# Optimize
optimizer = FIRE(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

# Print energies
for i, img in enumerate(images):
    print(f'Image {i}: Energy = {img.get_potential_energy():.6f} eV')
