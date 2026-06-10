from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

n2 = Atoms('N2', positions=[[0,0,0], [1.1,0,0]])
n2.set_calculator(EMT())

vib = Vibrations(n2)
vib.run()
freqs = vib.get_frequencies()

mass = 2 * 14.007 * 1.66054e-27  # kg
thermo = IdealGasThermo(mass=mass, frequencies=freqs, geometry='linear', symmetrynumber=2, temperature=298.15, pressure=1e5)
print(thermo.get_Gibbs_energy())
