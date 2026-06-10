from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

n2 = Atoms('N2', positions=[[0., 0., 0.], [0., 0., 1.1]])
n2.set_calculator(EMT())

vib = Vibrations(n2)
vib.run()
frequencies = vib.get_frequencies()
vib.clean()

thermo = IdealGasThermo(vib.get_zero_point_energy(), frequencies, n2,
                        geometry='linear', symmetrynumber=2, spin=0)
gibbs = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.)

print(f'Gibbs free energy: {gibbs:.5f} eV')
