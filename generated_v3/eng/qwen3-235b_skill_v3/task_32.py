from ase import units
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create H2O molecule
atoms = molecule('H2O')
atoms.calc = EMT()

# Optimize geometry
BFGS(atoms).run(fmax=0.01)

# Calculate vibrational modes
vib = Vibrations(atoms)
vib.run()

# Print frequency and energy for each mode
for i in range(len(vib.get_frequencies())):
    freq_cm = vib.get_frequencies()[i]
    energy_eV = vib.get_energies()[i]
    print(f"Mode {i+1}: {freq_cm:.1f} cm^-1, {energy_eV:.3f} eV")

# Cleanup
vib.clean()
