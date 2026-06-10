from ase import Atoms
from ase.calculators.emt import EMT
from ase.phonons import Phonons
from ase.thermochemistry import IdealGasThermo

# Set up the N2 molecule
n2 = Atoms('N2', positions=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.10]], calculator=EMT())

# Perform the vibrational frequency calculation
ph = Phonons(n2)
ph.run()
frequencies = ph.get_frequencies()

# Since Phonons might return positive and negative values (indicating instabilities),
# take the absolute value for frequencies that are real
vibrational_frequencies = [freq for freq in frequencies if freq > 0]

# Alternatively, if you want to filter only the positive ones for therapy (or consider >0 for logic)
# If none positive possibly recalc/check, but ideally should have one set positive for N2 

# Set up the thermochemistry calculator
thermo = IdealGasThermo(
    vib_energies=vibrational_frequencies,  # Potentially this would be [positive frequency values]
    geometry='linear',
    symmetrynumber=2,
    spin=0  # N2 has no unpaired electrons
)

# Calculate the Gibbs free energy at 298.15 K and 1 atm
gibbs_free_energy = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)  # Pressure in Pascal

# Print the Gibbs free energy
print(f"Gibbs free energy at 298.15 K and 1 atm: {gibbs_free_energy:.2f} eV")

# Note: Bigger symmetry handling or multiple vibrational mode systems might complicate, start from here.
