from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create FCC Ag structure
atoms = bulk('Ag', 'fcc', a=4.09)

# Define lattice constant range (7 points within +/-5%)
a0 = atoms.get_cell()[0, 0]
a_range = np.linspace(a0 * 0.95, a0 * 1.05, 7)

# Calculate energies
energies = []
volumes = []
calc = EMT()
atoms.set_calculator(calc)

for a in a_range:
    atoms.set_cell([a, a, a], scale_atoms=True)
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Calculate equilibrium lattice constant and bulk modulus
a_eq = (v0 / 4) ** (1/3)  # FCC has 4 atoms per cell
B_GPa = B / 1e9  # Convert to GPa

print(f'Equilibrium lattice constant: {a_eq:.4f} Å')
print(f'Bulk modulus: {B_GPa:.2f} GPa')
