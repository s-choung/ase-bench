from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = Atoms('Ag', [(0, 0, 0)], cell=(1, 1, 1), pbc=True)
atoms.calc = EMT()

a0 = atoms.get_cell()[0, 0]
volumes, energies = [], []
for factor in np.linspace(0.95, 1.05, 7):
    a = a0 * factor
    atoms.set_cell((a, a, a), scale_atoms=True)
    atoms.get_potential_energy()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0_fit = v0 ** (1 / 3)
print(f'Equilibrium lattice constant a0 = {a0_fit:.4f} Å')
print(f'Bulk modulus B = {B / 1e9:.2f} GPa')
