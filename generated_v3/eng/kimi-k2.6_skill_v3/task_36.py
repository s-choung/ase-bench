import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Ag', 'fcc', a=4.09, cubic=True)
cell = atoms.get_cell()
calc = EMT()
volumes, energies = [], []

for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = calc
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = v0 ** (1 / 3)
B_gpa = B * 160.21766208

print(f'Equilibrium lattice constant: {a0:.4f} Å')
print(f'Bulk modulus: {B_gpa:.1f} GPa')
