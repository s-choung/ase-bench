from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

ag = bulk('Ag', 'fcc', a=4.09)
ag.calc = EMT()

a0 = 4.09
volumes = []
energies = []

for scale in np.linspace(0.95, 1.05, 7):
    atoms = bulk('Ag', 'fcc', a=a0 * scale)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = (v0 * 4) ** (1/3)
B_GPa = B / 1.60218e-19 * 1e-9 * 1e30 * 1.60218e-19 / 1e9

from ase.units import GPa
B_GPa = B / GPa

print(f"평형 격자상수: {a_eq:.4f} Å")
print(f"Bulk Modulus: {B_GPa:.2f} GPa")
