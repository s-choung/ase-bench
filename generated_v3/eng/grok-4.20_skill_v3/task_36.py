from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms0 = bulk('Ag', 'fcc', a=4.09)
cell0 = atoms0.get_cell()
calc = EMT()
a_vals = np.linspace(0.95, 1.05, 7) * 4.09
volumes = []
energies = []

for a in a_vals:
    atoms = atoms0.copy()
    atoms.set_cell(cell0 * (a / 4.09), scale_atoms=True)
    atoms.calc = calc
    e = atoms.get_potential_energy()
    volumes.append(atoms.get_volume())
    energies.append(e)

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a0 = (v0 / 4)**(1/3)
B_gpa = B / units.GPa
print('Equilibrium lattice constant:', round(a0, 4), 'Å')
print('Bulk modulus:', round(B_gpa, 1), 'GPa')
