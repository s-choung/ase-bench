from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

cu = bulk('Cu', 'fcc')
calc = EMT()
volumes = []
energies = []
for a in np.linspace(3.4, 3.7, 7):
    cu.set_cell([a, a, a], scale_atoms=True)
    cu.set_calculator(calc)
    energies.append(cu.get_potential_energy())
    volumes.append(cu.get_volume())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B:.1f} GPa")
