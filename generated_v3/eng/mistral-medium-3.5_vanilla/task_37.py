from ase import Atoms
from ase.calculators.emt import EMT
from ase.thermochemistry import IdealGasThermo
from ase.vibrations import Vibrations

n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
n2.calc = EMT()
vib = Vibrations(n2)
vib.run()
vib_frequencies = vib.get_frequencies()

thermo = IdealGasThermo(vib_frequencies=vib_frequencies,
                        geometry='linear',
                        symmetrynumber=2)
gibbs_energy = thermo.get_gibbs_energy(temperature=298.15, pressure=1.0)
print(gibbs_energy)
