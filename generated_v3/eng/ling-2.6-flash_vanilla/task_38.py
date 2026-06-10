from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk
from ase.constraints import FixAtoms
from ase.thermochemistry import HarmonicThermo

# Create Cu bulk and attach EMT calculator
Cu = bulk('Cu', 'fcc', a=3.6)
Cu.calc = EMT()

# Fix all but one atom for vibrational frequency calculation
constraint = FixAtoms(indices=list(range(1, len(Cu))))
Cu.set_constraint(constraint)

# Get vibrational frequencies
vib = HarmonicThermo(Cu)
frequencies = vib.get_frequencies()
print("Frequencies (Hz):", frequencies)

# Compute Helmholtz free energy at 300 K
Cu.clear_constraint()
Cu.calc = EMT()
thermo = HarmonicThermo(Cu, frequencies=frequencies)
helmholtz_free_energy = thermo.get_helmholtz_energy(temperature=300)

print(f"Helmholtz free energy at 300 K: {helmholtz_free_energy:.6f} eV")
