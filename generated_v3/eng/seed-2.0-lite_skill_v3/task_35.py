from ase import Atoms
from ase.mep import NEB
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

# Manually create initial and final states: two fixed Al atoms, one moving Al
# Initial state: moving Al near left fixed Al
initial = Atoms('Al3',
                positions=[[0, 0, 0.0],   # Fixed left Al
                           [0, 0, 1.5],   # Moving Al
                           [0, 0, 6.0]],  # Fixed right Al
                cell=[10, 10, 10], pbc=False)

# Final state: moving Al near right fixed Al
final = Atoms('Al3',
              positions=[[0, 0, 0.0],
                         [0, 0, 4.5],
                         [0, 0, 6.0]],
              cell=[10, 10, 10], pbc=False)

# Create 3 total images (initial, intermediate, final)
images = [initial, initial.copy(), final]

# Apply constraints to fix the two end Al atoms in all images
for img in images:
    img.set_constraint(FixAtoms(indices=[0, 2]))
    img.calc = EMT()

# Set up and run NEB with linear interpolation
neb = NEB(images)
neb.interpolate(method='linear')
opt = BFGS(neb)
opt.run(fmax=0.05)

# Print energy of each optimized image
for idx, img in enumerate(images):
    print(f"Image {idx}: Energy = {img.get_potential_energy():.4f} eV")
