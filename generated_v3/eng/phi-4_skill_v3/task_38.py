from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create bulk Cu structure
atoms = bulk('Cu', 'fcc', a=3.63)
atoms.calc = EMT()

# Optimize the structure
opt = BFGS(atoms)
opt.run(fmax = 0.01)

# Create a Vibrations object and run it
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()  # cm^-1

# Obtain the energies and angles from the vibrations object
band_energies = vib.get_energies()  # eV

# Convert cm^-1 to eV for HarmonicThermo
frequencies_eV = frequencies * units.ev / (units.h * units.c * 100)

# Create HarmonicThermo object to calculate the Helmholtz free energy
thermo = HarmonicThermo(
    vib_energies=frequencies_eV,
    atoms=atoms,
    geometry='fcc',  # For bulk fcc structure
    symmetrynumber=1  # Assuming no symmetry reduction needed for bulk
)

# Calculate Helmholtz free energy at 300 K
T = 300.0  # Temperature in Kelvin
F = thermo.get_thermo_energy(T, 'F')  # Helmholtz free energy

# Print the vibrational frequencies and the Helmholtz free energy
print("Vibrational frequencies (cm^-1):")
print(frequencies)
print("\nHelmholtz free energy at 300 K (eV):")
print(F)
