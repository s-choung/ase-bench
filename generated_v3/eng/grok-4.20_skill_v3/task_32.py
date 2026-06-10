from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase import units
import numpy as np

atoms = Atoms('H2O', positions=[[0,0,0],[0.76,0,0],[0.38,0.58,0]])
atoms.center(vacuum=5.0)
atoms.calc = EMT()

BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms, name='vib_h2o')
vib.run()

freqs = vib.get_frequencies()
energies = vib.get_energies()

for i, (f, e) in enumerate(zip(freqs, energies)):
    print(f"Mode {i}: {f:.2f} cm^-1, {e:.4f} eV")

vib.clean()
