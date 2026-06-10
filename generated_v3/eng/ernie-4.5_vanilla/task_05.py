from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import StrainFilter
from ase.optimize.fire import FIRE as Optimizer
from ase.build import bulk
from ase.eos import EquationOfState

import numpy as np

# Create bulk copper in FCC structure
cu = bulk('Cu', 'fcc', a=3.6, cubic=True)

# Store initial volume
initial_volume = cu.get_volume()

# List to store energies and volumes
energies = []
volumes = []

calculator = EMT()

# Vary lattice constant
for strain in np.linspace(0.9, 1.1, 10):
    cu.set_cell(cu.cell * strain, scale_atoms=True)
    cu.set_calculator(calculator)
    energy = cu.get_potential_energy()
    volumes.append(cu.get_volume())
    energies.append(energy)

# Create EOS object and fit
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Output the results
print(f"Equilibrium volume (A^3): {v0:.2f}")
print(f"Bulk modulus (GPa): {B:.2f}")
