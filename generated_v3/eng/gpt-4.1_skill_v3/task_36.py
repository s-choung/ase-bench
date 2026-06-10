from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0 = 4.09  # Initial guess for Ag FCC lattice constant (Å)
atoms0 = bulk('Ag', 'fcc', a=a0)
cell = atoms0.get_cell()
volumes, energies, a_list = [], [], []

for x in np.linspace(0.95, 1.05, 7):
    a = a0 * x
    atoms = bulk('Ag', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())
    a_list.append(a)

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = a_list[np.argmin([abs(v-v0) for v in volumes])]
B_GPa = B / 100.0  # EMT: B in kbar; 1 kbar = 0.1 GPa

print(f'Equilibrium lattice constant: {a_eq:.4f} Å')
print(f'Bulk modulus: {B_GPa:.2f} GPa')
