from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

lattice_constants = np.linspace(3.5, 3.7, 15)
volumes = []
energies = []

for a in lattice_constants:
    cu = bulk('Cu', 'fcc', a=a)
    cu.calc = EMT()
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
B_GPa = B * 160.21766208
a0 = (4 * v0)**(1/3) / np.sqrt(2)

print(f"Equilibrium volume per atom: {v0/4:.4f} Å³")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
