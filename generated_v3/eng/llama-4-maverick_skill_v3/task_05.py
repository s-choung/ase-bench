import numpy as np
from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Initial guess for Cu FCC bulk
a0 = 3.6  # Angstrom
atoms = bulk('Cu', 'fcc', a=a0)
cell = atoms.get_cell()

# Calculate energy vs. volume
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# EOS fitting
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Print results
a_eq = (v0 * 4)**(1/3)  # For FCC, V = a^3 / 4
print(f'Equilibrium lattice constant: {a_eq:.3f} Å')
print(f'Equilibrium volume: {v0:.3f} Å³')
print(f'Bulk modulus: {B / units.GPa:.3f} GPa')
