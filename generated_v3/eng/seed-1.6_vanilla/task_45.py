from ase import Atoms
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

# Initialize H2 molecule
atoms = Atoms('H2', positions=[[0, 0, 0], [1.0, 0, 0]])
atoms.calc = EMT()

# Initial state
d_init = atoms.get_distance(0, 1)
e_init = atoms.get_potential_energy()
print(f'Initial: {d_init:.2f} Å, Energy: {e_init:.4f} eV')

# Apply bond length constraint and set to 0.9 Å
atoms.set_constraint(FixBondLength(0, 1))
atoms.set_distance(0, 1, 0.9)

# Constrained state
d_final = atoms.get_distance(0, 1)
e_final = atoms.get_potential_energy()
print(f'Constrained: {d_final:.2f} Å, Energy: {e_final:.4f} eV')
