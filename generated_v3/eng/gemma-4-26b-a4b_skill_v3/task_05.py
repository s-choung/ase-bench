import numpy as np
from ase.build import bulk
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# 1. Initialize Cu bulk and setup calculator
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# 2. Perform EOS fitting by varying volume
volumes = []
energies = []
original_cell = atoms.get_cell()

# Scan volume from 95% to 105% of initial volume
for scale in np.linspace(0.95, 1.05, 11):
    temp_atoms = atoms.copy()
    temp_atoms.set_cell(original_cell * scale, scale_atoms=True)
    temp_atoms.calc = EMT()
    volumes.append(temp_atoms.get_volume())
    energies.append(temp_atoms.get_potential_energy())

# 3. Fit Equation of State (Birch-Murnaghan)
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# 4. Output results
print(f"Equilibrium Volume: {v0:.4f} Å^3")
print(f"Bulk Modulus: {B/units.eV/units.A**-3:.4f} eV/Å^3") 
# Note: B is returned in units of energy/volume (eV/A^3)
