from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Create initial and final states
initial = Atoms('Al3', positions=[[0, 0, 0], [3, 0, 0], [1.5, 0, 0]])
final = Atoms('Al3', positions=[[0, 0, 0], [3, 0, 0], [2.5, 0, 0]])

# Fix the first two atoms
for atoms in [initial, final]:
    atoms.set_constraint()

# Set EMT calculator
initial.calc = EMT()
final.calc = EMT()

# Create images
images = [initial] + [initial.copy() for _ in range(3)] + [final]
for img in images[1:-1]:
    img.calc = EMT()

# Run NEB
neb = NEB(images)
neb.interpolate(method='linear')
opt = BFGS(neb, trajectory=None)
opt.run(fmax=0.05)

# Print energies
for i, img in enumerate(images):
    print(f"Image {i}: Energy = {img.get_potential_energy():.6f} eV")
