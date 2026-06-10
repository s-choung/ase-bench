from ase.calculators.emt import EMT
from ase.optim import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# N2 molecule
atoms = molecule("N2")
atoms.calc = EMT()

# Force field optimization
opt = BFGS(atoms)
opt.run(fmax=0.01)  # eV/Å

# Vibrational frequencies
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()  # cm⁻¹ (no parameter)
vib.clean()

# Gibbs free energy
thermo = IdealGasThermo(atoms=atoms, geometry="linear", symmetrynumber=2)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)  # Pa

print(f"Gibbs free energy G = {G:.4f} eV/atom")
