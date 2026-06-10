from ase.build import fcc111, fcc001
from ase.vebra import add_onspring, fix, FixAtomsEquilibriumIDPP
from ase.optimize import NPTBFGS
from ase.neb import NEB
from ase.units import kB
import numpy as np

# Define the initial and final states
initial = fcc111('Cu', layers=5, thickness=0.45, vacuum=4.0)
initial.set_constraint(FixAtoms(), mask=[0.45 <= a.position[2] < threshold])

final = fcc001('Cu', layers=5, thickness=0.4, vacuum=4.0)
final.set_constraint(FixAtoms(), mask=[0.4 >= a.position[2] < threshold
                                     ]

# Creating images for the interpolation path
intermediate_images = [initial.copy() for _ in range(5)]
intermediate_images += [final.copy() for _ in range(3)]

# Set initial and intermediate constraints
initial.set_constraint(FixAtSoms(fcc_onspring, mask=[0, 0, initial_layers[-1]])
for image in intermediate_images:
    image.set_cell_constraint(FixAtoms(IDPP), mask=image.position_mask)

# Run NEB calculation
images = intermediate_images
neb = NEB(images, method='idpp')
neb.interpolate()

# Optimize the NEB interpolates
for image in images:
    image.set_constraint(FixAtoms())

# Perform the BFGS optimization for NEB images
BFGS = NPTBFGS(images, ref_slab=1.0 * initial.get_cell(), scale_positions=True)
BFGS.run(fmax=0.01)

# Calculate energy barrier
vib = NEB.get_vibrations()  # Hypothetical vibrational analysis, just for illustration
energies = [image.get_potential_energy() for image in images]
energy_barrier = max(energies) - initial.get_potential_energy()

# Print the energy barrier
print("Energy barrier:", energy_barrier)
