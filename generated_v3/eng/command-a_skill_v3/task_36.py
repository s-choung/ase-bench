import numpy as np
from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Create Ag FCC bulk structure
atoms = bulk('Ag', 'fcc', a=4.09)
atoms.calc = EMT()

# Define lattice constant range
a0 = atoms.cell.lengths()[0]
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell([x * a0, x * a0, x * a0], scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Convert bulk modulus to GPa
B_GPa = B / units.GPa

# Print results
print(f'Equilibrium lattice constant: {v0**(1/3):.4f} Å')
print(f'Bulk modulus: {B_GPa:.2f} GPa')
