from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Initial state: Al atom at (0,0,0), moving atom at (1,0,0), fixed Al at (5,0,0)
initial = Atoms('Al3', positions=[[0,0,0], [1,0,0], [5,0,0]])
# Final state: Al atom at (0,0,0), moving atom at (4,0,0), fixed Al at (5,0,0)
final = Atoms('Al3', positions=[[0,0,0], [4,0,0], [5,0,0]])

# Create 5 images including initial and final
images = [initial] + [initial.copy() for _ in range(3)] + [final]

# Fix first and third atoms in all images
for img in images:
    img.set_constraint(FixAtoms(indices=[0, 2]))
    img.calc = EMT()

# Create NEB with linear interpolation
neb = NEB(images)
neb.interpolate(method='linear')

# Optimize with BFGS
opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

# Print energies
for i, img in enumerate(images):
    print(f"Image {i}: Energy = {img.get_potential_energy():.5f} eV")
