from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Create N2 molecule
n2 = Atoms('N2')
n2.center(vacuum=5.0)

# Set EMT calculator
n2.calc = EMT()

# Optimize geometry
from ase.optimize import BFGS
opt = BFGS(n2)
opt.run(fmax=0.05)

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
frequencies = vib.get_frequencies()  # in cm^-1

# Compute Gibbs free energy using IdealGasThermo
thermo = IdealGasThermo(vib_energies=frequencies, atoms=n2,
                        geometry='linear', symmetrynumber=2,
                        temperature=298.15, pressure=101325)
G = thermo.get_gibbs_energy()

print(f"Vibrational frequencies (cm⁻¹): {frequencies}")
print(f"Gibbs free energy at 298.15 K and 1 atm: {G:.3f} kJ/mol")
