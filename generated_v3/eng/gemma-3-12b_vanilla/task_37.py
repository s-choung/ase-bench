from ase import Atoms
from ase.calculators.emt import EMT
from ase.thermo import IdealGasThermo

n2 = Atoms('N2', geometry='linear', pbc=False, symmetrynumber=2)
calc = EMT()
n2.calc = calc
n2.get_potential_energy()
freq = n2.get_frequencies()
thermo = IdealGasThermo(freq)
g = thermo.get_gibbs_free_energy(298.15, 1.01325)
print(g)
