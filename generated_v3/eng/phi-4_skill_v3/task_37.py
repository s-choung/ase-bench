from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Create N2 molecule
atoms = molecule('N2')

# Set calculator
atoms.calc = EMT()

# Optimize geometry
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()  # frequencies in cm⁻¹
vib.clean()  # remove the extra temp directory

# Print vibrational frequencies
print("Vibrational frequencies (cm⁻¹):", freqs)

# Convert vibrational frequencies to vibrational energies (eV)
vib_energies = np.dot(freqs, [11604.52500617])  # 1 cm⁻¹ = 0.00012398426 eV

# Compute Gibbs free energy
thermo = IdealGasThermo(vib_energies=vib_energies, atoms=atoms,
                        geometry='linear', symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

# Print Gibbs free energy result
print("Gibbs free energy at 298.15K and 1 atm (eV):", G)
