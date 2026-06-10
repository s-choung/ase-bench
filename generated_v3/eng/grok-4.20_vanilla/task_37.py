from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

atoms = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
atoms.calc = EMT()

vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()

thermo = IdealGasThermo(vib_energies=vib.get_energies(),
                        potentialenergy=atoms.get_potential_energy(),
                        atoms=atoms, geometry='linear',
                        symmetrynumber=2, spin=0)

gibbs = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0)
print(gibbs)
