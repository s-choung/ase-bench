from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create Cu bulk structure
atoms = bulk('Cu', cubic=True)
atoms.calc = EMT()

# Compute vibrational frequencies
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()

# Use only positive frequencies (exclude translational modes near zero)
positive_freqs = [freq for freq in frequencies if freq > 1e-3]

# Create thermo instance and compute Helmholtz free energy
thermo = HarmonicThermo(phonon_energies=positive_freqs, potential_energy=atoms.get_potential_energy())
F = thermo.get_helmholtz_energy(temperature=300)

print(f"{F:.6f}")
