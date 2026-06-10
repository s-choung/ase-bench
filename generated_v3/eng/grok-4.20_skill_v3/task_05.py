from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

cell = atoms.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 9):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    e = a.get_potential_energy()
    volumes.append(a.get_volume())
    energies.append(e)

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a0 = (v0 * 4)** (1/3)
print('Equilibrium volume:', v0)
print('Bulk modulus:', B)
print('Equilibrium lattice constant:', a0)
