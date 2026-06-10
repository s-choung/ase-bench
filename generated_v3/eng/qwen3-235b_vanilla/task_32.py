from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.units import invcm, eV

# Create H2O molecule with approximate geometry
atoms = Atoms('H2O', positions=[(0, 0, 0), (0.96, 0, 0), (0, 0.96, 0)])

# Center atoms and add vacuum
atoms.center(vacuum=5.0)

# Use EMT calculator
atoms.calc = EMT()

# Calculate vibrational modes
vib = Vibrations(atoms)
vib.run()

# Print frequencies and energies
for mode in range(9):
    freq = vib.get_frequency(mode)
    if abs(freq) > 1e-3:
        print(f"Mode {mode}: {freq:.2f} cm^-1, {freq * invcm / eV:.6f} eV")

vib.clean()
