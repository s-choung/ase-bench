import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.thermochemistry import IdealGasThermo
from ase.build import molecule
from ase.vibrations import Vibrations

# Create N2 molecule
n2 = molecule('N2')
n2.calc = EMT()

# Optimize the structure
bfgs = Atoms.BFGS(n2)
bfgs.run(fmax=0.01)  # Optimize cell and positions

# Calculate vibrational frequencies
vib = Vibrations(n2, name='vib')
vib.run()
freqs = vib.get_frequencies()

# Calculate Gibbs free energy at 298.15K and 1 atm
thermo = IdealGasThermo(vib_energies=freqs, atoms=n2, geometry='linear', symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print("Vibrational Frequencies (cm⁻¹):", freqs)
print("Gibbs Free Energy (eV):", G)
