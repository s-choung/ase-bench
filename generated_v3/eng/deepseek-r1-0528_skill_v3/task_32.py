from ase.build import molecule
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.calculators.emt import EMT

atoms = molecule('H2O')
atoms.center(vacuum=5.0)
atoms.calc = EMT()

opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='vib')
vib.run()
vib_energies = vib.get_energies()
vib_frequencies = vib.get_frequencies()

vib.summary()
vib.clean()

print("Vibrational modes:")
for i, (freq, energy) in enumerate(zip(vib_frequencies, vib_energies)):
    if i < 3:  # Skip first 3 modes (translation/rotation)
        continue
    print(f"Mode {i-2}: Frequency = {freq:.2f} cm⁻¹, Energy = {energy:.6f} eV")
