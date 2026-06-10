import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Ag', 'fcc', a=4.0)
steps = np.linspace(0.95, 1.05, 7)
volumes, energies = [], []

for factor in steps:
    a = atoms.cell.lengths()[0] * factor
    newatoms = atoms.copy()
    newatoms.set_cell([a, a, a], scale_atoms=True)
    newatoms.set_calculator(EMT())
    energy = newatoms.get_potential_energy()
    vol_per_atom = (a**3) / len(newatoms)
    energy_per_atom = energy / len(newatoms)
    volumes.append(vol_per_atom)
    energies.append(energy_per_atom)

eos = EquationOfState(volumes, energies, fmt='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (v0 * len(atoms)) ** (1/3)
print(f'Equilibrium lattice constant (a0): {a0:.4f} Å')
print(f'Bulk modulus (B): {B:.2f} GPa')
