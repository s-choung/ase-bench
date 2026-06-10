from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Define initial and final states
initial = Atoms('AlAlAl', positions=[(0,0,0), (2,0,0), (1,0,0)], cell=(4,4,4), pbc=True)
final = Atoms('AlAlAl', positions=[(0,0,0), (2,0,0), (1,1,0)], cell=(4,4,4), pbc=True)

# Create images and interpolate
images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate('linear')

# Set constraints and calculator
for img in images:
    img.set_constraint(FixAtoms(indices=[0,1]))
    img.calc = EMT()

# Optimize pathway
BFGS(neb).run(fmax=0.01)

# Print energies
for i, img in enumerate(images):
    print(f"Image {i}: {img.get_potential_energy():.3f} eV")
