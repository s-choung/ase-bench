import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

a0_guess = 4.09
atoms = bulk('Ag', 'fcc', a=a0_guess)
atoms.calc = EMT()

scales = np.linspace(0.95, 1.05, 7)
volumes = []
energies = []
for s in scales:
    a = atoms.copy()
    a.set_cell(a.get_cell() * s, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = v0 ** (1/3)
B_GPa = B * units.GPa
print(f'Equilibrium lattice constant: {a_eq:.3f} Å')
print(f'Bulk modulus: {B_GPa:.1f} GPa')
