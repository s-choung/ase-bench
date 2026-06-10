from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create bulk copper atoms
atoms = bulk('Cu', cubic=True)
atoms.calc = EMT()

# Perform structure optimization
atoms.get_potential_energy(force_consistent=True)

# Calculate vibrational frequencies
vib = Vibrations(atoms, name='vib')
vib.run()
vib_energies = vib.get_energies()

# Calculate Helmholtz free energy at 300K using HarmonicThermo
thermo = HarmonicThermo(vib_energies=vib_energies, atoms=atoms)
F = thermo.get_helmholtz_energy(temperature=300)  # in eV

print(F)
