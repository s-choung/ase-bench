from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.units import Hartree, eV, mol, kcal, kJ, Bohr, Angstrom
import numpy as np

# H2O molecule
atoms = Atoms('H2O', positions=[
    [0.0, -0.757, 0.587],
    [0.0, 0.757, 0.587],
    [0.0, 0.0, 0.0]
])

# Center in a large box
atoms.center(vacuum=5.0)

# EMT calculator (Note: EMT is for metals, not H2O; will likely fail for H/O)
calc = EMT()
atoms.calc = calc

# Vibrations calculation
vib = Vibrations(atoms)
vib.run()
vib.summary()

# Print frequencies in cm^-1 and energies in eV
energies = vib.get_energies()
print("\nVibrational Modes:")
for i, E in enumerate(energies):
    freq_cm = E / (Hartree * eV) * 8065.54429  # Convert eV to cm^-1
    print(f"Mode {i+1}: {freq_cm:.2f} cm^-1, {E:.6f} eV")

vib.clean()
