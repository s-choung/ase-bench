import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Setup Cu bulk structure
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()

# Compute Helmholtz free energy at 300K
# vib.get_thermal_properties returns (entropy, free_energy_correction)
# Total Helmholtz F = E_stat + F_vib
# Note: HarmonicThermo is typically used with phonon DOS or frequencies
# Here we manually compute using the frequencies directly via thermodynamic principles
temp = 300
kB = 8.617333262e-5  # eV/K

# Get static energy
e_static = atoms.get_potential_energy()

# Calculate vibrational contribution to Helmholtz free energy (F_vib)
# F_vib = sum [ kBT * ln(2 sinh(h*nu / 2kBT)) ]
# Using frequency in THz (standard for ASE)
nu_thz = frequencies / 1e12
h = 4.135667e-15  # eV*s
c = 2.99792458e8  # m/s
# Convert THz to energy units (h*nu)
# h_planck_ev_s * nu_hz = energy_ev
h_planck = 4.135667e-15
h_nu = h_planck * (nu_thz * 1e12)

# Avoid log(0) for zero modes
h_nu = np.where(h_nu < 1e-9, 1e-9, h_nu)

# F_vib formula: sum(kBT * ln(1 - exp(-h*nu/kBT)) + 0.5 * h*nu)
x = h_nu / (kB * temp)
f_vib = np.sum(kB * temp * np.log(1 - np.exp(-x)) + 0.5 * h_nu)

total_f = e_static + f_vib

print(f"Static Energy: {e_static:.4f} eV")
print(f"Vibrational Free Energy contribution: {f_vib:.4f} eV")
print(f"Total Helmholtz Free Energy at 300K: {total_f:.4f} eV")

# Cleanup
vib.clean()
