from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
for freq, energy in zip(vib.get_frequencies(), vib.get_energies()):
    print(f"{freq:10.3f} cm^-1  {energy:10.6f} eV")
vib.clean()
