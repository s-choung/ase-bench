from ase.build import bulk
from ase.calculators.emt import EMT
from ase.thermochemistry import HarmonicThermo

# Create bulk Cu with experimental lattice constant
atoms = bulk('Cu', a=3.61, cubic=True)
atoms.calc = EMT()

# Get total energy (reference)
energy = atoms.get_potential_energy()

# Create Vibrations object for phonon calculation
from ase.vibrations import Vibrations
vib = Vibrations(atoms, name='vib')
vib.run()

# Get vibrational frequencies
frequencies = vib.get_frequencies()

# Convert frequencies from Hz to eV (1 Hz = 4.135667696e-15 eV)
frequencies_eV = frequencies * 4.135667696e-15

# Create HarmonicThermo and compute Helmholtz free energy at 300K
thermo = HarmonicThermo(frequencies_eV, temperature=300)
free_energy = thermo.get_free_energy()

print(f"Vibrational frequencies (eV): {frequencies_eV}")
print(f"Helmholtz free energy at 300K: {free_energy} eV")
