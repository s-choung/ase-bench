from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
cell = atoms.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (v0 / 4.0) ** (1/3)  # FCC 4 atoms/cell
print(f'Equilibrium lattice constant (Å): {a0:.4f}')
print(f'Equilibrium volume (Å³): {v0:.4f}')
print(f'Bulk modulus (GPa): {B/1e9*1.60218e-19*1e30:.2f}')  # B [eV/Å³] → GPa
