from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
for i, freq in enumerate(vib.get_frequencies()):
    print(f'Mode {i+1}: {freq:.2f} cm^-1, {vib.get_energies()[i]:.3f} eV')
