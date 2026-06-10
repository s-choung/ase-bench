from ase import molecule
from ase.calculators.emt import EMT
from ase.thermo import IdealGasThermo

atoms = molecule('N2', geometry='linear')
atoms.calc = EMT()
thermo = IdealGasThermo(atoms, temperature=298.15, pressure=1, symmetrynumber=2)
print(thermo.get_gibbs_free_energy())
