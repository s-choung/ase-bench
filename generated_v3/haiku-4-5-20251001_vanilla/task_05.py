from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import CalculateEOS
import numpy as np

cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()

eos = CalculateEOS(cu, trajectory='cu_eos.traj')
v, e, B = eos.fit()

print(f"Equilibrium volume: {v:.4f} Å³")
print(f"Bulk modulus: {B:.4f} eV/Å³")

a_eq = (4 * v) ** (1/3)
print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
