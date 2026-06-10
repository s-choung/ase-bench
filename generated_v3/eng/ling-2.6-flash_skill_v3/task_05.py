from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
calc = EMT()

vols, E = [], []
for x in np.linspace(0.9, 1.1, 11):
    a_tmp = atoms.copy()
    a_tmp.set_cell(a_tmp.get_cell() * x, scale_atoms=True)
    a_tmp.calc = calc
    vols.append(a_tmp.get_volume())
    E.append(a_tmp.get_total_energy())

eos = EquationOfState(vols, E, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f'Equilibrium volume: {v0:.4f} Å^3')
print(f'Bulk modulus: {B:.4f} eV/Å^3')
