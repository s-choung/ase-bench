from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
volumes, energies = [], []

for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(a.cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f"Equilibrium volume: {v0} Å³")
print(f"Bulk modulus: {B} eV/Å³")
