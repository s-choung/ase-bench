from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.visualize import view

# Create initial and final states with a moving Al atom
initial = Atoms('Al3', positions=[[0, 0, 0], [2.7, 0, 0], [1.35, 1.35, 0]])
final = Atoms('Al3', positions=[[0, 0, 0], [2.7, 0, 0], [1.35, -1.35, 0]])

# Fix the first and last atoms
for atom in [initial[0], initial[-1]]:
    atom.fixed = True
for atom in [final[0], final[-1]]:
    atom.fixed = True

# Assign EMT calculator
initial.calc = EMT()
final.calc = EMT()

# Create NEB with 3 images
images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate(method='linear')

# Optimize and print energies
from ase.optimize import BFGS
dyn = BFGS(neb, trajectory='neb.traj')
dyn.run(fmax=0.05)

for i, img in enumerate(images):
    print(f"Image {i}: Energy = {img.get_potential_energy():.4f} eV")
