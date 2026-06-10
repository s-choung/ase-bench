from ase import Atoms
from ase.neb import NEB
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

# Initial and final states
initial = Atoms('Al3', positions=[[0, 0, 0], [0, 0, 3], [0, 0, 0.5]])
final = Atoms('Al3', positions=[[0, 0, 0], [0, 0, 3], [0, 0, 2.5]])

# Create images with 1 intermediate
images = [initial, initial.copy(), final]
neb = NEB(images)
neb.interpolate()

# Set constraints and calculator
for img in images:
    img.set_constraint(FixAtoms(indices=[0, 1]))
    img.calc = EMT()

# Run NEB optimization
BFGS(neb).run(fmax=0.05)

# Print energies
for i, img in enumerate(images):
    print(f"Image {i} Energy: {img.get_potential_energy():.4f} eV")
