from ase import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms, name='cu_vib')
vib.run()
freqs = vib.get_frequencies()

thermo = HarmonicThermo(vib_energies=0.5 * np.array(freqs) * units.kB * 1e-2,
                        potentialenergy=atoms.get_potential_energy(),
                        atoms=atoms)
A = thermo.get_helmholtz_energy(temperature=300)
print(A)
