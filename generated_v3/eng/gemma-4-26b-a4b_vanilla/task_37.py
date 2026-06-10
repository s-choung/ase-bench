from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# Create N2 molecule (using EMT, though it's for metals, we follow instructions)
mol = Atoms('N2', positions=[[0, 0, -0.5], [0, 0, 0.5]])
mol.set_calculator(EMT())

# Calculate vibrational frequencies
vib = Vibrations(mol)
vib.run()
freqs = vib.get_frequencies()
vib.clean()

# Get total energy from calculator
energy = mol.get_potential_energy()

# Define thermochemistry parameters
# Note: EMT is not physical for N2, but we use it as requested
# IdealGasThermo expects frequencies in Hz (or rad/s depending on version, 
# but ASE uses Hz for the thermochem module)
thermo = IdealGasThermo(
    energy, 
    freqs, 
    mass=mol.get_mass(), 
    natoms=len(mol), 
    geometry='linear', 
    symmetrynumber=2
)

# Compute Gibbs Free Energy at 298.15K and 1 atm
# IdealGasThermo.get_gibbs returns G in eV
gibbs_ev = thermo.get_gibbs(temperature=298.15, pressure=101325)

print(f"Vibrational Frequencies: {freqs} Hz")
print(f"Gibbs Free Energy at 298.15K, 1 atm: {gibbs_ev} eV")
