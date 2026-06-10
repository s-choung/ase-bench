from ase import Atoms
from ase.calculators.emt import EMT
from ase.thermo import IdealGasThermo

# N₂ molecule (linear, experimental symmetry number 2)
mol = Atoms('N2', positions=[[0,0,0], [0,0,1.0978]], cell=[5,5,5], pbc=False)

EMT().calculate(mol)

freqs = mol.get_frequencies()
print('Predicted vibrational frequencies (cm^-1):')
print(freqs)

# Gibbs free energy at 298.15 K, 1 atm
thermo = IdealGasThermo(mol, temp=298.15, press=1.0)
gibbs = thermo.gibbs_energy()[0] / mol.get_volume()  # approximate per unit volume
print(f'Gibbs free energy (per unit cell volume) = {gibbs:.4f} eV')  # or convert to kJ/mol as needed
