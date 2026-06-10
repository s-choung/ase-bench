from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Set up the N2 molecule
n2 = molecule('N2')
n2.calc = EMT()

# Vibrational analysis
vib = Vibrations(n2)
vib.run()

# Extract vibrational frequencies
frequencies = vib.get_frequencies()

# Thermochemistry calculations
thermo = IdealGasThermo(vib_energies=frequencies,
                        potentialenergy=n2.get_potential_energy(),
                        atoms=n2,
                        geometry='linear',
                        symmetrynumber=2,
                        spin=0)

# Compute Gibbs free energy at 298.15 K and 1 atm
gibbs_energy = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

# Clean up the temporary files created by Vibrations
vib.clean()

print(f'Gibbs free energy at 298.15K and 1 atm: {gibbs_energy:.2f} eV')
