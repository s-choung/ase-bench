import numpy as np
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase.units import kJ, mol, invcm

# Build N2 and attach EMT calculator
atoms = molecule('N2')
atoms.set_calculator(EMT())

# Compute vibrational frequencies (in cm⁻¹)
vib = Vibrations(atoms, name='N2_vib')
vib.run()
freqs = vib.get_frequencies()
print('Vibrational frequencies (cm⁻¹):', freqs)

# Convert frequencies to vibrational energies (eV)
vib_energies = freqs * invcm

# IdealGasThermo for Gibbs free energy
thermo = IdealGasThermo(vib_energies,
                        geometry='linear',
                        symmetrynumber=2,
                        atoms=atoms,
                        spin=0)

# T = 298.15 K, P = 1 atm ≈ 1.01325 bar
G = thermo.get_gibbs_energy(298.15, 1.01325)  # returns energy in eV
print(f'Gibbs free energy at 298.15 K, 1 atm: {G:.4f} eV')
print(f'Gibbs free energy at 298.15 K, 1 atm: {G * kJ / mol:.4f} kJ/mol')
