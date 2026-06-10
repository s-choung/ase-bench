from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()

opt = BFGS(atoms, trajectory=None)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='vib_h2o')
vib.run()

freqs = vib.get_frequencies()
energies = vib.get_energies()

print("Mode | Frequency (cm^-1) | Energy (eV)")
print("-" * 45)
for i, (f, e) in enumerate(zip(freqs, energies)):
    print(f"  {i:2d} |  {f.real:>14.4f}     | {e.real:>10.6f}")

vib.summary()
vib.clean()
