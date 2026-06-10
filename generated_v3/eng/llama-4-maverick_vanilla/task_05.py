from ase import Atoms
from ase.build import bulk
from ase.eos import EquationOfState
from ase.calculators.emt import EMT

cu = bulk('Cu', 'fcc')
eos = EquationOfState([cu.copy() for _ in range(7)], EMT())
v0, e0, B = eos.fit()
print(f'Equilibrium volume: {v0:.2f} Ang^3')
print(f'Bulk modulus: {B:.2f} GPa')
