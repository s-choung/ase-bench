from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create FCC Cu bulk structure
atoms = bulk('Cu', 'fcc')

# Calculator
calc = EMT()
atoms.calc = calc

# List to store volumes and energies
volumes = []
energies = []

# Generate structures with varying lattice constants
for a in np.linspace(3.5, 4.0, 5):
    atoms_copy = atoms.copy()
    atoms_copy.set_cell(atoms.cell * (a / atoms.cell[0, 0]), scale_atoms=True)
    atoms_copy.calc = calc
    energies.append(atoms_copy.get_potential_energy())
    volumes.append(atoms_copy.get_volume())

# Fit EOS
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

# Print results
print(f"Equilibrium volume: {v0:.2f} Å³")
print(f"Bulk modulus: {B:.2f} eV/Å³")
