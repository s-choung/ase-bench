from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

volumes, energies = [], []
a_list = np.linspace(3.5, 3.7, 9)
for a in a_list:
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B:.3f} eV/Å³")
