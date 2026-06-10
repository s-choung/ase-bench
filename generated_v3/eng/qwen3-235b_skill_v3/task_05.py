from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create FCC Cu bulk structure
atoms = bulk('Cu', 'fcc')

# Assign EMT calculator
atoms.calc = EMT()

# Define lattice constant variation range
volumes = []
energies = []
cell = atoms.cell.copy()

for a in np.linspace(3.4, 3.8, 5):
    atoms.set_cell(cell * (a / 3.6), scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Fit EOS
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

# Print results
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B:.3f} eV/Å³")
