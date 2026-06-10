from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
from ase.units import kJ, kcal, eV, K
import numpy as np

# Create Cu bulk structure
atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

# Optimize geometry
opt = BFGS(atoms)
opt.run(fmax=0.05)

# Compute vibrational frequencies
vib = Vibrations(atoms, name='vib')
vib.run()
freqs = vib.get_frequencies() * (2 * np.pi * 1.0 / 1024.527)  # Convert to cm⁻¹ if needed, but not necessary here

# Harmonic free energy
heat_capacity = HarmonicThermo(vib.vibrations, atoms=atoms, geometry='nonlinear', symmetrynumber=4, spin=0)
F = heat_capacity.get_thermal_energy(temperature=300 * K)
print(f"Helmholtz free energy at 300K: {F / eV:.4f} eV")
