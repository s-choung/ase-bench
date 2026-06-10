from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import numpy as np

cu = bulk('Cu', 'fcc', a=3.615)
supercell = cu * (2, 2, 2)
supercell.calc = EMT()

vib = Vibrations(supercell)
vib.run()

energies = abs(vib.get_energies())
energies.sort()
if energies[2] < 1e-6:
    energies = energies[3:]

thermo = HarmonicThermo(frequencies=energies, units='eV')
F = thermo.get_helmholtz_free_energy(300)
print(f"{F:.6f}")
