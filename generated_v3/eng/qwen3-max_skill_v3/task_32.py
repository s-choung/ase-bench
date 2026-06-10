from ase import molecule
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

for f, e in zip(freqs, energies):
    print(f"{f:.2f} cm^-1  {e:.6f} eV")

vib.clean()
