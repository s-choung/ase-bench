from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

calc = EMT()
a_test = np.linspace(3.4, 3.9, 12)      # range of lattice constants
volumes, energies = [], []

for a in a_test:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = calc
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies)
V0, E0, B0 = eos.fit()          # V0 in Ang^3, B0 in eV/Ang^3

print(f'Equilibrium volume: {V0:.4f} Ang^3')
print(f'Bulk modulus:       {B0:.2f} eV/Ang^3')
