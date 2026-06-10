from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import ase.units as units
import numpy as np

# Build N2 molecule
n2 = molecule('N2')
n2.calc = EMT()

# Optimize the geometry
from ase.optimize import BFGS
opt = BFGS(n2)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(n2, name='vib')
vib.run()
vib_energies = vib.get_frequencies()

# Calculate Gibbs free energy
thermo = IdealGasThermo(vib_energies=vib_energies, atoms=n2,
                        geometry='linear', symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(G)
