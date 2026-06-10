import numpy as np
from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

a0 = 4.09  # Initial lattice constant for Ag
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    atoms = bulk('Ag', 'fcc', a=a0 * x, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = (v0 * 4)**(1/3)  # For FCC, V = a^3 / 4
B_GPa = B / units.GPa
print(f'Equilibrium lattice constant: {a_eq:.3f} Å')
print(f'Bulk modulus: {B_GPa:.1f} GPa')
