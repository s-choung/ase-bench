from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# Create N2 molecule
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
n2.calc = EMT()

# Optimize geometry
from ase.optimize import BFGS
opt = BFGS(n2)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
 vib = Vibrations(n2)
 vib.run()
 vib_energies = vib.get_energies()

# Remove zero modes and keep real positive frequencies
vib_energies = vib_energies[2:]  # Remove 5 zero modes (3 trans + 2 rot for linear)
vib_energies = vib_energies[vib_energies > 0]

# Get electronic energy and rotational symmetry number
energy = n2.get_potential_energy()
thermo = IdealGasThermo(vib_energies=vib_energies,
                        potentialenergy=energy,
                        atoms=n2,
                        geometry='linear',
                        symmetrynumber=2)

# Calculate Gibbs free energy at 298.15 K and 1 atm
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0)
print(G)

# Clean up vibration files
vib.clean()
