from ase import Atoms
from ase.calculation import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Define N2 molecule
n2 = Atoms('N', positions=[(0, 0, 0), (1.1, 0, 0)], cell=[10, 10, 10], pbc=True)

# Set up EMT calculator
n2.calc = EMT()

# Optimize geometry
n2.optimize()

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
freqs = vib.get_frequencies()

# Compute Gibbs free energy
thermo = IdealGasThermo(vib_energies=vib.get_energies(), atoms=n2, geometry='linear', symmetrynumber=2)
gibbs_free_energy = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

# Print Gibbs free energy
print(f"Gibbs free energy at 298.15K and 1 atm: {gibbs_free_energy:.4f} eV")
