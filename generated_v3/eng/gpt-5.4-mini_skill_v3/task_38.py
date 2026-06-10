import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms, name='cu_vib')
vib.run()
freqs = vib.get_frequencies()
vib_energies = vib.get_energies()
vib.clean()

thermo = HarmonicThermo(vib_energies=vib_energies)
F = thermo.get_helmholtz_energy(temperature=300.0)

print(f"{F:.6f} eV")
