from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
n2.set_calculator(EMT())
n2.get_potential_energy()

vib = Vibrations(n2)
vib.run()
freqs = vib.get_frequencies()
vib.summary()

thermo = IdealGasThermo(vib_energies=freqs, geometry='linear',
                        symmetrynumber=2, atoms=n2)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f"Gibbs free energy: {G:.6f} eV")
