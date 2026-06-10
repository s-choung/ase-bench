from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build and optimize H2O
atoms = molecule('H2O')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, name='h2o_vib')
vib.run()
freqs = vib.get_frequencies()      # cm⁻¹
energies = vib.get_energies()      # eV

for i, (f, e) in enumerate(zip(freqs, energies), 1):
    print(f"Mode {i}: {f:.2f} cm⁻¹, {e:.4f} eV")

vib.clean()
