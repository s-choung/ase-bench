from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

n2 = molecule('N2')
n2.calc = EMT()

vib = Vibrations(n2)
vib.run()
vib_freq = vib.get_frequencies()

thermo = IdealGasThermo(vib_energies=vib_freq, geometry='linear', symmetrynumber=2, atoms=n2)
g = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f"Gibbs free energy: {g:.6f} eV")
