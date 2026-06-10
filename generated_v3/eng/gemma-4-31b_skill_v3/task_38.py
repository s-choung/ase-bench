import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# 1. Structure Setup and Optimization
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# 2. Vibrational Analysis
vib = Vibrations(atoms, name='cu_vib')
vib.run()
frequencies = vib.get_frequencies() # cm-1
energies = vib.get_energies()       # eV
vib.clean()

# 3. Thermodynamic Calculation
# HarmonicThermo expects vibrational energies in eV
thermo = HarmonicThermo(vib_energies=energies, atoms=atoms)
f_helmholtz = thermo.get_helmholtz_energy(temperature=300)

print(f"Helmholtz Free Energy at 300K: {f_helmholtz:.6f} eV")
