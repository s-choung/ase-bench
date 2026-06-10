from ase import Atoms
from ase.calculation import HarmonicThermo
from ase.calculators import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np

# Generate Cu bulk structure
atoms = Atoms('Cu', cell='fcc', a=3.5668, pbc=True)

# Set up EMT calculator
atoms.calc = EMT()

# Optimize geometry
BFGS(atoms).run(fmax=0.01)

# Compute HarmonicThermo
thermo = HarmonicThermo(atoms)

# Get vibrational frequencies
freqs = thermo.get_frequencies()  # in cm^-1

# Compute Helmholtz free energy at 300K
e0 = thermo.get_total_energy()  # in eV
temperature = 300  # in K
free_energy = e0 - kBT * np.log(np.prod(freqs)) + 3 / 2 * np.sum(freqs) * h / 2.014e-15  # Constants in eV

# Print the result
print(f"Helmholtz Free Energy at 300K: {free_energy:.4f} eV")
