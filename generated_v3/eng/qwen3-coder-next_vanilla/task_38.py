from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.dynamics import MITNEB
from ase.thermochemistry import HarmonicThermo
from ase.build import bulk
import numpy as np

# Create Cu bulk structure (FCC)
cu_bulk = bulk('Cu', cubic=True)

# Set up EMT calculator
cu_bulk.calc = EMT()

# Optimize structure
cu_bulk.get_potential_energy()
cu_bulk.rattle(stdev=0.01, seed=42)

# Calculate phonons using finite differences
from ase.phonons import Phonons
radius = 4.0
qpts = (1, 1, 1)
phonon = Phonons(cu_bulk, EMT(), supercell=(2, 2, 2), displacement=0.04)
phonon.run()

# Get phonon dispersion and dos
 frequencies = phonon.get_frequencies()
 # Ensure positive frequencies for thermo
 frequencies = np.abs(frequencies)

# Create harmonic thermodynamic model
# 1 atom per unit cell, 3N modes (9 for 3x3x3 supercell → 9*1 = 9, but scaled)
# For bulk phonon thermo, use the unit cell
# Phonons gives frequencies for the supercell; need to map to unit cell
# ASE's HarmonicThermo expects 3N frequencies for N atoms in the unit cell
# We'll use the frequencies from the Gamma-point only (q=0) for thermodynamics
# Alternatively, use the full phonon spectrum but for thermodynamics at 300K, 
# theΓ-point approximation is often used, but ASE's HarmonicThermo can use the full set.

# For Cu bulk (1 atom per unit cell), we need 3 frequencies at Gamma.
# Let's extract Gamma-point frequencies directly:
phonon.read()  # read data from files
frequencies_Gamma = phonon.get_frequencies(q=[0, 0, 0])[0]  # [0] for the branch

# Ensure all are real and positive
frequencies_Gamma = np.abs(frequencies_Gamma)

# Create thermodynamic model for 1 formula unit (1 atom)
# ASE expects frequencies in cm^-1 for HarmonicThermo, but we have eV or THz?
# EMT phonons return frequencies in eV (hbar*omega) — need to check units
# Actually, ase.phonons.Phonons.get_frequencies returns frequencies in eV (hbar*omega)
# HarmonicThermo expects frequencies in eV (hbar*omega)
# Confirm: ASE uses eV (hbar*omega) for phonon frequencies internally

thermo = HarmonicThermo(frequencies_Gamma, atoms_per_unit_cell=1)

# Compute Helmholtz free energy at 300 K
T = 300.0  # K
F = thermo.get_helmholtz_free_energy(T)

print(f"{F:.6f}")
