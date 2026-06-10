from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# Create N2 molecule
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
n2.calc = EMT()
n2.center(vacuum=5.0)

# Vibrational analysis
vib = Vibrations(n2)
vib.run()
frequencies = vib.get_frequencies()  # in cm^-1

# Energies
energy = n2.get_potential_energy()

# Thermochemistry
thermo = IdealGasThermo(
    vibrational_frequencies=frequencies * 1.0,  # cm^-1
    potentialenergy=energy,
    atoms=n2,
    geometry='linear',
    symmetrynumber=2,
    spin=0
)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.)

print(f"Gibbs free energy at 298.15 K and 1 atm: {G:.6f} eV")

vib.clean()  # cleanup
