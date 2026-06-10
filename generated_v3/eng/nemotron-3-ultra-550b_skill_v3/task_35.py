from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

# Initial state: Al atom at x=1.5 between fixed atoms at x=0 and x=3
initial = Atoms('Al3', positions=[(0, 0, 0), (1.5, 0, 0), (3, 0, 0)])
initial.set_constraint(FixAtoms(indices=[0, 2]))

# Final state: Al atom moved to x=2.5 (near right atom)
final = Atoms('Al3', positions=[(0, 0, 0), (2.5, 0, 0), (3, 0, 0)])
final.set_constraint(FixAtoms(indices=[0, 2]))

# Create 5 images total: initial + 3 intermediate + final
images = [initial] + [initial.copy() for _ in range(3)] + [final]

neb = NEB(images)
neb.interpolate(method='idpp')

# Assign calculator to intermediate images only (endpoints keep constraints)
for img in images[1:-1]:
    img.calc = EMT()

opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

# Print energies
for i, img in enumerate(images):
    print(f'Image {i}: {img.get_potential_energy():.4f} eV')
