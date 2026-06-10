from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms, name='h2o_vib')
vib.run()

freqs = vib.get_frequencies()
energies = vib.get_energies()

print(f"{'Mode':>6} {'Frequency (cm^-1)':>22} {'Energy (eV)':>18}")
for i, (f, e) in enumerate(zip(freqs, energies)):
    print(f"{i:>6} {f.real:>22.4f} {e.real:>18.6f}")

vib.summary()
vib.clean()
