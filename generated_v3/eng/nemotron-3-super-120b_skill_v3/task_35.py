from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

# Fixed Al atoms positions
fixed1 = (0.0, 0.0, 0.0)
fixed2 = (2.0, 0.0, 0.0)

# Initial state: moving Al near left fixed atom
initial = Atoms(
    symbols=['Al', 'Al', 'Al'],
    positions=[fixed1, fixed2, (0.5, 0.0, 0.0)]
)
# Final state: moving Al near right fixed atom
final = Atoms(
    symbols=['Al', 'Al', 'Al'],
    positions=[fixed1, fixed2, (1.5, 0.0, 0.0)]
)

# Constrain the two fixed Al atoms (indices 0 and 1)
constraint = FixAtoms([0, 1])
initial.set_constraint(constraint)
final.set_constraint(constraint)

# Attach EMT calculator
initial.calc = EMT()
final.calc = EMT()

# Create images: initial + one intermediate + final (3 images total)
images = [initial, initial.copy(), final]
# Set calculator and constraint for the intermediate image
images[1].set_constraint(constraint)
images[1].calc = EMT()

# NEB with linear interpolation
neb = NEB(images)
neb.interpolate(method='linear')

# Optimize the path
optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

# Print energies of each image
for i, img in enumerate(images):
    e = img.get_potential_energy()
    print(f'Image {i}: energy = {e:.4f} eV')
