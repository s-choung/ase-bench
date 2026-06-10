import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.md import MDLogger, Langevin
from ase.md.nptberendsen import NPTBerendsen
from ase.build import bulk

# Create the FCC aluminum supercell
a = 4.05  # lattice constant in Angstrom
al = bulk('Al', 'fcc', a=a)
al *= (2, 2, 2)

# Setup the calculator
al.set_calculator(EMT())

# Define the temperature and pressure
T = 500  # Temperature in Kelvin
P = 10e3  # Pressure in MPa
k_B = 8.617333262145e-5  # Boltzmann constant in eV/K
V_initial = al.get_volume()

# Convert pressure unit from GPa to eV/Ang^3
P = P/10**3 * 1.602176634e-19 / ((a**3) * 1e-30)

# Run NPT MD simulation
dyn = NPTBerendsen(al, T=T, P=P, ttime=1.0, pfactor=0.05)
dyn.run(100)

V_final = al.get_volume()
print(f'Initial cell volume: {V_initial} Angstrom^3')
print(f'Final cell volume: {V_final} Angstrom^3')
