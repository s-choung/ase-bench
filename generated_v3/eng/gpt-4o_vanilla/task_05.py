from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0 = 3.6
cu_bulk = bulk('Cu', 'fcc', a=a0)
cu_bulk.set_calculator(EMT())

volumes = []
energies = []

for delta in np.linspace(-0.05, 0.05, 10):
    cu_bulk.set_cell(cu_bulk.get_cell() * (1 + delta), scale_atoms=True)
    volumes.append(cu_bulk.get_volume())
    energies.append(cu_bulk.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a_eq = (v0 / 4) ** (1 / 3) * 2 ** 0.5

print(f'Equilibrium volume: {v0:.2f} Å³')
print(f'Equilibrium lattice constant: {a_eq:.2f} Å')
print(f'Bulk modulus: {B:.2f} eV/Å³')
