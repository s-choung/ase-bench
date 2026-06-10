from ase import Atoms
from ase.calculators.emt import EMT
from ase.calculators.cgcvb import CGCVB
from ase.vibrations import Vibrations
from ase.calculators.thermo import IdealGasThermo

# Create an N2 molecule with EMT calculator
n2 = Atoms('N2', positions=[(0, 0, 0)])
n2.set_calculator(EMT())
n2.set_cell([[3.0, 0, 0], [0, 3.0, 0], [0, 0, 3.0]])

# Perform phonon calculations using CG-CVB
n2.set_calculator(CGCVB(calc=Coulombian()))
vib = Vibrations(n2)
frequencies = vib.get_frequencies()

# Set vibrational frequencies to IdealGasThermo
th = IdealGasThermo(temperature=298.15, pressure=0, mode='npg', energy=(frequencies > 0).sum())
th.set_atoms(n2)
th.attach(n2)

# Calculate the Gibbs free energy
gibbs_free_energy = th.get_thermal_properties()['Gibbs free energy at T']
print(f'Vibrational Frequencies: {frequencies}')
print(f'Gibbs Free Energy at 298.15 K and 1 atm: {gibbs_free_energy}')
