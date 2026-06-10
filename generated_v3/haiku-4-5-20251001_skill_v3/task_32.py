from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

atoms = molecule('H2O')
atoms.calc = EMT()

opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='h2o_vib')
vib.run()

frequencies = vib.get_frequencies()
energies = vib.get_energies()

print("H2O Vibrational Modes")
print("=" * 50)
print(f"{'Mode':<6} {'Frequency (cm⁻¹)':<20} {'Energy (eV)':<15}")
print("=" * 50)
for i, (freq, energy) in enumerate(zip(frequencies, energies)):
    print(f"{i+1:<6} {freq:<20.2f} {energy:<15.6f}")
print("=" * 50)

vib.clean()
