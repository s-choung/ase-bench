from ase import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# Set up N2 molecule and calculator
atoms = molecule('N2')
atoms.calc = EMT()

# Optimize geometry
BFGS(atoms).run(fmax=0.01)

# Compute vibrational frequencies
vib = Vibrations(atoms)
vib.run()
vib_freqs = vib.get_frequencies()

# Filter out negative and near-zero frequencies
vib_energies = [f for f in vib.get_energies() if f > 1e-4]

# Clean up vibration files
vib.clean()

# Compute Gibbs free energy
thermo = IdealGasThermo(vib_energies=vib_energies,
                        atoms=atoms,
                        geometry='linear',
                        symmetrynumber=2,
                        spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(G)
