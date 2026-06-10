from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create H2 molecule
h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
h2.calc = EMT()

# Compute initial energy and bond length
initial_energy = h2.get_potential_energy()
initial_bond_length = h2.get_distance(0, 1)

# Apply constraint to fix bond length to 0.9 angstroms
h2.set_constraint(FixBondLength(0, 1))
h2.set_distance(0, 1, 0.9)

# Recalculate energy
constrained_energy = h2.get_potential_energy()
constrained_bond_length = h2.get_distance(0, 1)

# Output
print(f"Initial Bond Length: {initial_bond_length:.2f} Å, Energy: {initial_energy:.2f} eV")
print(f"Constrained Bond Length: {constrained_bond_length:.2f} Å, Energy: {constrained_energy:.2f} eV")
