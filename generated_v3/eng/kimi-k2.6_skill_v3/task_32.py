from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()

BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()

for freq, energy in zip(vib.get_frequencies(), vib.get_energies()):
    print(f"{freq:.4f} cm^-1   {energy:.6f} eV")
