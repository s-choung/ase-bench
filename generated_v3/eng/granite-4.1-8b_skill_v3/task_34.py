from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import fcc111, add_adsorbate
from ase.neb import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# Define the Cu(111) surface with 2x2 unit cell and 5 Å vacuum
surface = fcc111('Cu', size=(2, 2, 1), vacuum=10.0)

# Position of the adatom on the fcc hollow site (surface normal direction z)
hollow_fcc = [1.26, 1.26, 0.5]  # Approximate nearest-neighbor distance / 2
surface += add_adsorbate(surface, 'Cu', height=1.6, position='hollow')
initial_atoms = surface.copy()

# Fix the substrate atoms
mask = [atom.tag >= 3 for atom in initial_atoms]  # tags >= 3 are substrate atoms
initial_atoms.set_constraint(FixAtoms(mask=mask))

# Define the target hcp hollow site
hcp_hollow = [0.0, 1.26, 0.5]  # Example position for hcp hollow on Cu(111)
final_atoms = initial_atoms.copy()
final_atoms.positions[:, 0] = hcp_hollow[0]
final_atoms.positions[:, 1] = hcp_hollow[1]
final_atoms.positions[:, 2] = hcp_hollow[2]

# Set up the NEB with 5 images (initial + final + 3 intermediate)
images = [initial_atoms.copy() for _ in range(5)]
images[0].positions[:, -1] = hollow_fcc
images[-1].positions[:, -1] = hcp_hollow
for image in images[1:-1]:
    image.calc = EMT()
    image.cell = initial_atoms.cell

neb = NEB(images)
neb.interpolate(method='idpp')  # IDPP interpolation for the path

# Optimize the NEB images
neb.attach(FixAtoms(mask=mask))  # fix substrate atoms during NEB optimization
neb.calc = EMT()
opt = BFGS(neb)
opt.run(fmax=0.05)  # Optimization tolerance

# Retrieve energies of the images
energies = [image.get_potential_energy() for image in images]

# Calculate the diffusion barrier
max_energy = np.max(energies)
initial_energy = energies[0]
barrier = max_energy - initial_energy

print(f"Energy barrier for Cu adatom diffusion (hollow to hollow): {barrier:.4f} eV")
