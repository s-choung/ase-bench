from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()

energies = vib.get_energies()
frequencies = vib.get_frequencies()

print(f"{'Mode':>4} {'Frequency (cm^-1)':>20} {'Energy (eV)':>15}")
for i, (f, e) in enumerate(zip(frequencies, energies)):
    print(f"{i:>4} {f.real:>20.2f} {e.real:>15.4f}")

vib.clean()
