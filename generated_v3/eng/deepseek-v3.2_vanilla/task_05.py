import ase.units as units
from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

symbol = 'Cu'
a_guess = 3.6
cell = np.array([[0, a_guess/2, a_guess/2],
                 [a_guess/2, 0, a_guess/2],
                 [a_guess/2, a_guess/2, 0]])
atoms = Atoms(symbol, positions=[[0, 0, 0]], cell=cell, pbc=True)
atoms = atoms.repeat((2, 2, 2))

volumes = []
energies = []
for eps in np.linspace(-0.1, 0.1, 9):
    a = a_guess * (1 + eps)
    cell = np.array([[0, a/2, a/2],
                     [a/2, 0, a/2],
                     [a/2, a/2, 0]])
    atoms.set_cell(cell, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
B = B / units.GPa
a0 = (4 * v0)**(1/3)

print(f'Equilibrium lattice constant: {a0:.4f} Å')
print(f'Equilibrium volume: {v0:.2f} Å³')
print(f'Bulk modulus: {B:.2f} GPa')
