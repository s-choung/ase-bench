from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase import units

# Create H2 molecule with initial bond length
h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])

# Calculate initial energy and bond length
h2.calc = EMT()
initial_energy = h2.get_potential_energy()
initial_bond_length = h2.get_distance(0, 1)

# Apply FixBondLength constraint
h2.set_constraint(FixBondLength(0, 1, 0.9))

# Calculate energy with constraint
constrained_energy = h2.get_potential_energy()
constrained_bond_length = h2.get_distance(0, 1)

# Print results
print(f"Initial bond length: {initial_bond_length:.3f} Å")
print(f"Initial energy: {initial_energy:.4f} eV")
print(f"Constrained bond length: {constrained_bond_length:.3f} Å")
print(f"Constrained energy: {constrained_energy:.4f} eV")
