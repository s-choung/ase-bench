from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.001)

vib = Vibrations(atoms, name='vib_cu')
vib.run()
freqs = vib.get_frequencies()
vib_energies = np.array([f * units.invcm for f in freqs if f > 1.0])

thermo = HarmonicThermo(vib_energies, electronicenergy=0.0)
F = thermo.get_helmholtz_free_energy(temperature=300.0)
print(F)
vib.clean()
