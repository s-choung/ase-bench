from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()

BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()

freqs = vib.get_frequencies()
energies = vib.get_energies()

for i, (f, e) in enumerate(zip(freqs, energies)):
    print(f"Mode {i}: {f:8.2f} cm^-1, {e:8.4f} eV")

vib.clean()
