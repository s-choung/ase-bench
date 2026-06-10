from ase import Atoms
from ase.neb import NEB
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Fixed atoms: Al at (0,0,0) and (3,0,0)
d = 3.0
fixed_positions = [(0, 0, 0), (d, 0, 0)]

# Initial state: moving atom at (1.5, 1.0, 0)
initial = Atoms('Al3', 
                positions=fixed_positions + [(d/2, 1.0, 0)],
                cell=[6, 4, 4], pbc=False)
initial.set_constraint([0, 1])  # Fix first two atoms

# Final state: moving atom at (1.5, -1.0, 0)
final = Atoms('Al3',
              positions=fixed_positions + [(d/2, -1.0, 0)],
              cell=[6, 4, 4], pbc=False)
final.set_constraint([0, 1])

# Create NEB with 3 images (total 5 including endpoints)
images = [initial]
for i in range(3):
    image = initial.copy()
    image.calc = EMT()
    images.append(image)
images.append(final)

neb = NEB(images)
neb.interpolate()

# Attach calculator to intermediate images
for img in images[1:-1]:
    img.calc = EMT()

# Optimize
opt = BFGS(neb)
opt.run(fmax=0.05)

# Print energies
print("Image energies (eV):")
for i, img in enumerate(images):
    if i == 0 or i == len(images)-1:
        img.calc = EMT()
    print(f"  Image {i}: {img.get_potential_energy():.6f}")
