from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import FIRE

# Fixed Al atoms
fixed = Atoms('Al2', positions=[(0, 0, 0), (4, 0, 0)])

# Initial and final states with moving Al
initial = fixed.copy()
initial.append(Atoms('Al', positions=[(1, 0, 0)]))  # near left fixed atom

final = fixed.copy()
final.append(Atoms('Al', positions=[(3, 0, 0)]))   # near right fixed atom

# Constraint: keep the two fixed Al atoms immobile
constraint = FixAtoms([0, 1])

# Create three images (initial, intermediate, final)
images = [initial.copy(), initial.copy(), final.copy()]
for im in images:
    im.set_constraint(constraint)
    im.calc = EMT()

# Linear interpolation for the middle image
images[1].set_positions((initial.get_positions() + final.get_positions()) / 2)

# NEB setup
neb = NEB(images, climb=False)
neb.interpolate()  # ensure linear interpolation

# Optimize the band
opt = FIRE(neb)
opt.run(fmax=0.05)

# Print energies
for i, im in enumerate(images):
    print(f'Image {i}: {im.get_potential_energy():.3f} eV')
