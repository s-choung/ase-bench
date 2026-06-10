import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
cell = atoms.get_cell()
volumes, energies = [], []

for sf in np.linspace(0.95, 1.05, 9):
    a = atoms.copy()
    a.set_cell(cell * sf, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a0 = v0 ** (1/3)
print(f'Equilibrium lattice constant: {a0:.4f} Å')
print(f'Equilibrium volume: {v0:.4f} Å³')
print(f'Bulk modulus: {B/units.GPa:.2f} GPa')
