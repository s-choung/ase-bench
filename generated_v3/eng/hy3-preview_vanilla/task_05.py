import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Generate Cu FCC structures with varied lattice constants
a0 = 3.6  # Initial guess (Å)
volumes = []
energies = []
calc = EMT()

for scale in np.linspace(0.95, 1.05, 10):
    a = a0 * scale
    cu = bulk('Cu', 'fcc', a=a)
    cu.calc = calc
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())

# Fit Equation of State
eos = EquationOfState(volumes, energies, 'birchmurnaghan')
v0, e0, B = eos.fit()
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B:.2f} eV/Å³ ({B*160.2:.1f} GPa)")
