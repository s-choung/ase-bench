from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0 = 4.09
atoms = bulk('Ag', 'fcc', a=a0)
atoms.calc = EMT

scales = np.linspace(0.95, 1.05, 7)
volumes, energies = [], []

for s in scales:
    a = a0 * s
    at = bulk('Ag', 'fcc', a=a)
    at.calc = EMT
    volumes.append(at.get_volume())
    energies.append(at.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = (4.0 * v0) ** (1.0 / 3.0)
B_GPa = B * 160.21766208

print(f"Equilibrium lattice constant: {a_eq:.6f} Å")
print(f"Bulk modulus: {B_GPa:.6f} GPa")
