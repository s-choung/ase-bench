from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# Create N2 molecule
n2 = Atoms('N2', positions=[[0, 0, 0], [1.1, 0, 0]])
n2.set_calculator(EMT())

# Optimize geometry
n2.get_potential_energy()
n2.constraints = None

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
freqs = vib.get_frequencies()

# Remove imaginary frequencies (should be none for N2)
freqs_real = freqs[~np.iscomplex(freqs)].real

# Calculate thermodynamic properties
thermo = IdealGasThermo(
    freqs_real,
    geometry='linear',
    symmetrynumber=2,
    atoms=n2,
    electronic_energy=0.0
)

# Get Gibbs free energy at 298.15K and 1 atm
gibbs_energy = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(gibbs_energy)
