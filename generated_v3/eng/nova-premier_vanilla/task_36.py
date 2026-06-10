from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Silver FCC lattice
atoms = Atoms('Ag', cell=[[0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]], pbc=True)
calc = EMT()

# Lattice variation
a0 = atoms.get_cell_lengths_and_angles()[0]
volumes = []
energies = []
for x in np.linspace(-0.05, 0.05, 7):
    a = a0 * (1 + x)
    atoms.set_cell([a, a, a], scale_atoms=True)
    atoms.calc = calc
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# EOS fitting
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a_eq = (4 * v0 / np.sqrt(2))**(1/3)
print(f"Equilibrium lattice constant: {a_eq:.3f} Ang")
print(f"Bulk modulus: {B / 1e9:.1f} GPa")
