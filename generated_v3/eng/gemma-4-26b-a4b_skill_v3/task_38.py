import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# 1. Setup Cu bulk and optimize
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
# Use FrechetCellFilter for bulk optimization (cell + positions)
from ase.filters import FrechetCellFilter
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# 2. Vibrational analysis
vib = Vibrations(atoms, name='vib_cu')
vib.run()
energies = vib.get_energies()  # eV
# Note: For bulk, frequencies are typically treated as phonons, 
# but using HarmonicThermo as requested for the vibrational modes found.
# freq_cm_inv = vib.get_frequencies()

# 3. Thermochemistry
# HarmonicThermo requires energies, atoms, and geometry/symmetry info
# For a periodic bulk, we treat the modes as a set of oscillators
thermo = HarmonicThermo(vib_energies=energies, atoms=atoms, 
                        geometry='non-linear', symmetrynumber=1, spin=0)

# Helmholtz free energy (A) at 300K
# In ASE, get_gibbs_energy(P) returns G = A + PV. 
# For a solid at standard pressure, A approx G.
# To get A specifically, we use P=0 or subtract PV.
A_300K = thermo.get_gibbs_energy(temperature=300.0, pressure=0.0)

print(f"Helmholtz Free Energy at 300K: {A_300K:.6f} eV")

vib.clean()
