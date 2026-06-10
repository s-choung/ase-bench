from ase import Atoms
from ase.io import write
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase.calculators.emt import EMT
import numpy as np

# Build N2 molecule
n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
n2.calc = EMT()

# Optimize structure
opt = BFGS(n2)
opt.run(fmax=0.01)

# Compute vibrational frequencies
vib = Vibrations(n2, name='n2')
vib.run()
vib_energies = vib.get_energies() * 0.001  # Convert to eV
vib.clean()

# Calculate Gibbs free energy
thermo = IdealGasThermo(vib_energies=vib_energies,
                        atoms=n2,
                        geometry='linear',
                        symmetrynumber=2,
                        spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(f'Gibbs free energy = {G:.6f} eV')
