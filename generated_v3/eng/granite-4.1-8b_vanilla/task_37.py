from ase import Atoms
from ase.calculators.emt import EMT
from ase.calculations.vibspectrum import calculate_frequencies
from ase.eos import EquationOfState
from ase.units import kcal, mol, angstrom, g, atm, K
from chemex.thermo import IdealGasThermo

# Create N2 molecule
n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1 * angstrom)])

# Assign EMT calculator
n2.calc = EMT()

# Calculate vibrational frequencies
n2_vib = calculate_frequencies(n2)

# Extract the frequency of the N2 stretching mode
frequency = n2_vib[0]  # First vibrational mode is the N2 stretch

# Compute equilibrium properties using EMT
eos = EquationOfState(n2, calculator=n2.calc)
p, v, eos = eos.fit()
v_mean = v  # Mean volume

# Calculate equilibrium bond length from volume
bond_length = (v_mean * 2 / (2 * n2.get_mass()))**(1/3) * angstrom

# Set up IdealGasThermo for N2
ideal_gas = IdealGasThermo(
    T0=298.15 * K,
    P0=1 * atm,
    H0=0,
    S0=0,
    Cp=29.1 * (kcal / mol / K),
    units='cgs'
)

# Compute Gibbs free energy at 298.15 K and 1 atm
G = ideal_gas.get_gibbs_energy(T=298.15 * K, P=1 * atm)

# Apply symmetry correction (symmetry number = 2 for N2)
G_corrected = G / 2

# Print the corrected Gibbs free energy
print(f"Corrected Gibbs free energy of N2 at 298.15 K and 1 atm: {G_corrected:.2f} kcal/mol")
