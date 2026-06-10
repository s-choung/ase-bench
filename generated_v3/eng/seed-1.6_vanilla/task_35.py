from ase import Atoms
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import FIRE

# Fixed Al atoms (indices 0,1)
constraints = FixAtoms(indices=[0, 1])

# Initial state: third Al at (1,0,0)
initial = Atoms('Al3', positions=[(0,0,0), (3,0,0), (1,0,0)], constraints=constraints)
initial.calc = EMT()

# Final state: third Al at (2,0,0)
final = Atoms('Al3', positions=[(0,0,0), (3,0,0), (2,0,0)], constraints=constraints)
final.calc = EMT()

# 3 NEB images with linear interpolation
images = [initial.copy(), initial.copy(), final.copy()]
neb = NEB(images)
neb.interpolate()

# Assign calculator to all images
for img in images:
    img.calc = EMT()

# Run NEB optimization
opt = FIRE(neb)
opt.run(fmax=0.05)

# Print image energies
for idx, img in enumerate(images):
    print(f'Image {idx}: Energy = {img.get_total_energy():.6f} eV')
