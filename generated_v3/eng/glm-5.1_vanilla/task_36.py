from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0 = 4.09
volumes, energies = [], []

for a in np.linspace(0.95 * a0, 1.05 * a0, 7):
    ag = bulk('Ag', 'fcc', a=a, cubic=True)
    ag.calc = EMT()
    energies.append(ag.get_potential_energy())
    volumes.append(ag.get_volume())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = v0**(1/3)
B_GPa = B * 160.21766208

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
