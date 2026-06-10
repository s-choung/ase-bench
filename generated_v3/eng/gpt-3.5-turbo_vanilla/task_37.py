from ase.build import molecule
from ase.calculators.emt import EMT
from ase.thermochemistry import IdealGasThermo

N2 = molecule('N2')
N2.set_calculator(EMT())
vib_freq = N2.get_vibrational_frequencies(geometry='linear', symmetrynumber=2)

thermo = IdealGasThermo(vib_freq)
Gibbs_free_energy = thermo.get_gibbs_energy(298.15, 1e5)  # 298.15K and 1 atm

print(Gibbs_free_energy)
