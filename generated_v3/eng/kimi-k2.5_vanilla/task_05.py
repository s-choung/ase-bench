from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

volumes, energies = [], []
for sf in np.linspace(0.9, 1.1, 7):
    a = 3.6 * sf
    tmp = bulk('Cu', 'fcc', a=a, cubic=True)
    tmp.calc = EMT()
    volumes.append(tmp.get_volume())
    energies.append(tmp.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

print(f'Equilibrium volume: {v0:.4f} Å³')
print(f'Bulk modulus: {B*160.22:.2f} GPa')
print(f'Equilibrium lattice constant: {v0**(1/3):.4f} Å')
