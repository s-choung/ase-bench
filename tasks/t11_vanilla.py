"""T11 Vanilla: Equation of state fitting for bulk Cu"""
from ase.build import bulk
from ase.calculators.emt import EMT
import numpy as np

volumes = []
energies = []
for a in np.linspace(3.4, 3.8, 7):
    cu = bulk('Cu', 'fcc', a=a)
    cu.calc = EMT()
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())

from ase.utils.eos import EquationOfState
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print(f"Equilibrium volume: {v0:.2f} Å³")
print(f"Equilibrium energy: {e0:.4f} eV")
print(f"Bulk modulus: {B:.4f} eV/ų")
