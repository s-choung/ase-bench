from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

a_vals = np.linspace(3.4, 3.9, 7)
volumes, energies = [], []

for a in a_vals:
    atoms.set_cell([a, a, a], scale_atoms=True)
    volumes.append(atoms.get_volume() / len(atoms))
    energies.append(atoms.get_potential_energy() / len(atoms))

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (4 * v0) ** (1/3)
B_GPa = B * 160.21766

print(f'Equilibrium volume per atom: {v0:.4f} Å³')
print(f'Equilibrium energy per atom:  {e0:.4f} eV')
print(f'Bulk modulus: {B_GPa:.2f} GPa')
print(f'Equilibrium lattice constant: {a0:.4f} Å')
