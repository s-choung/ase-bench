from ase import Atoms
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Initial state: 2 fixed Al, moving Al near left fixed atom
initial = Atoms(
    symbols='Al3',
    positions=[[0, 0, 0], [8, 0, 0], [2.9, 0, 0]],
    cell=[10, 10, 10],
    pbc=False
)
initial.set_constraint(FixAtoms(indices=[0, 1]))

# Final state: moving Al near right fixed atom
final = Atoms(
    symbols='Al3',
    positions=[[0, 0, 0], [8, 0, 0], [5.1, 0, 0]],
    cell=[10, 10, 10],
    pbc=False
)
final.set_constraint(FixAtoms(indices=[0, 1]))

# Relax end point geometries
for end in [initial, final]:
    end.calc = EMT()
    BFGS(end).run(fmax=0.05)

# Create 3 NEB images with linear interpolation
images = [initial] + [initial.copy() for _ in range(1)] + [final]
neb = NEB(images)
neb.interpolate(method='linear')

# Set EMT calculator for all images
for img in images:
    img.calc = EMT()

# Optimize NEB path
BFGS(neb).run(fmax=0.05)

# Print energy of each image
print("NEB Image Energies:")
for i, img in enumerate(images):
    print(f"Image {i}: {img.get_potential_energy():.4f} eV")
