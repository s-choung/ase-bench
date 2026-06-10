import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

cell = atoms.get_cell()
volumes, energies = [], []

for x in np.linspace(0.90, 1.10, 11):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

from ase import units
a0 = (v0 / 4) ** (1/3)  # cubic FCC: 4 atoms per cell

print(f"평형 부피 V0       : {v0:.4f} Å³")
print(f"평형 격자상수 a0   : {a0:.4f} Å")
print(f"체적탄성계수 B     : {B / units.GPa:.2f} GPa")
