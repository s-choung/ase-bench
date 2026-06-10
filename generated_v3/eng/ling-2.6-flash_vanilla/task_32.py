from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.phonons import Phonons
import numpy as np

# Create H2O molecule with reasonable geometry
atoms = Atoms('H2O', positions=[[0.0, 0.0, 0.1], [0.0, 0.9, -0.6], [0.0, -0.9, -0.6]])
atoms.set_calculator(EMT())

# Relax geometry
dyn = BFGS(atoms)
dyn.run(fmax=0.01)

# Apply periodic boundary conditions for phonon calculation
atoms.set_cell([8.0, 8.0, 8.0])
atoms.set_pbc([True, True, True])

# Center the molecule in the cell
center = atoms.get_center_of_mass()
atoms.positions -= center

# Calculate phonons
phonons = Phonons(atoms)
phonons.run(mode='small', delta=0.01)

# Get frequencies
frequencies = phonons.get_frequencies()

# Filter out translations and rotations (near zero frequencies)
tol = 10.0  # cm^-1 threshold
vibrational_modes = []
for freq in frequencies.flatten():
    if abs(freq) > tol:
        vibrational_modes.append(freq)

# Convert to eV: E(eV) = h * c * wavenumber
h_c = 1.23984193e-4  # eV*cm
print("Vibrational modes:")
for freq in sorted(vibrational_modes):
    energy = h_c * freq
    print(f"Frequency: {freq:.1f} cm^-1, Energy: {energy:.6f} eV")
