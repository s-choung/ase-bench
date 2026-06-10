from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochem import IdealGasThermo
import numpy as np

# Setup N2 molecule
atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
atoms.calc = EMT()

# Relax geometry
from ase.optimize import BFGS
BFGS(atoms).run(fmax=0.01)

# Calculate vibrational frequencies
vibs = Vibrations(atoms)
vibs.run()
frequencies = vibs.get_frequencies()
# Convert cm-1 to Hz
freqs_hz = frequencies * 29979245800

# Thermodynamic calculation
thermo = IdealGasThermo(
    freqs=freqs_hz,
    geometry='linear',
    symmetrynumber=2,
    T=298.15,
    P=101325
)

print(f"Gibbs Free Energy: {thermo.get_gibbs_free_energy()} J/mol")
