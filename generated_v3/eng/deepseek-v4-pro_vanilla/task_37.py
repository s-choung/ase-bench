from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Set up N2 molecule
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
n2.calc = EMT()

# Calculate vibrational frequencies
vib = Vibrations(n2, name='n2_vib')
vib.run()
vib_energies = vib.get_energies()

# Extract frequencies in eV
frequencies = vib_energies[-1]  # The stretching mode

# Compute ideal gas thermodynamics
thermo = IdealGasThermo(
    vib_energies=vib_energies,
    geometry='linear',
    symmetrynumber=2,
    atoms=n2
)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=1.01325e5, verbose=False)
print(f"Gibbs free energy of N2 at 298.15 K and 1 atm: {G:.6f} eV")
