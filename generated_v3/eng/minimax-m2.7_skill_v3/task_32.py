from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms, name='vib_H2O')
vib.run()

freqs = vib.get_frequencies()
energies = vib.get_energies()

print(f"{'Mode':<6} {'Frequency (cm^-1)':<20} {'Energy (eV)':<15}")
print("-" * 45)
for i, (f, e) in enumerate(zip(freqs, energies)):
    print(f"{i:<6} {f:<20.2f} {e:<15.6f}")

vib.summary()
vib.clean()
