from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB

# Fixed atoms at ends, moving atom in the middle
init = Atoms('Al3',
             positions=[[0, 0, 0], [4, 0, 0], [2, 0, 0]],
             cell=[6, 6, 6], pbc=False)
final = Atoms('Al3',
             positions=[[0, 0, 0], [4, 0, 0], [3, 0, 0]],
             cell=[6, 6, 6], pbc=False)

# Keep the two end atoms fixed
fix = FixAtoms(mask=[True, True, False])
init.set_constraint(fix)
final.set_constraint(fix)

# Images: initial, one interpolated middle, final
images = [init] + [init.copy() for _ in range(1)] + [final]

# Assign EMT calculator to every image
for img in images:
    img.calc = EMT()

# NEB setup with linear interpolation
neb = NEB(images)
neb.interpolate(method='linear')

# Optimize the band
BFGS(neb).run(fmax=0.05, steps=200)

# Print energies of all images
for i, img in enumerate(images):
    print(f'Image {i}: {img.get_potential_energy():.6f} eV')
