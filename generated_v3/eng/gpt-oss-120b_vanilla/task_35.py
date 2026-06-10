from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS

# Fixed left and right Al atoms, moving middle Al atom
initial = Atoms('Al3', positions=[(0, 0, 0), (2.0, 0, 0), (4, 0, 0)])
final   = Atoms('Al3', positions=[(0, 0, 0), (3.0, 0, 0), (4, 0, 0)])

# Freeze the outer atoms
c = FixAtoms(indices=[0, 2])
initial.set_constraint(c)
final.set_constraint(c)

# Assign calculator
calc = EMT()
initial.set_calculator(calc)
final.set_calculator(calc)

# Create images (initial + 1 intermediate + final)
images = [initial] + [initial.copy() for _ in range(1)] + [final]

# Linear interpolation of the moving atom
neb = NEB(images, climb=True)
neb.interpolate()

# Optimize the band
opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

# Print energies of each image
for i, img in enumerate(images):
    print(f'Image {i}: {img.get_potential_energy():.6f} eV')
