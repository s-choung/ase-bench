from ase.build import molecule
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

# Create an H2 molecule
h2 = molecule('H2')
h2.calc = EMT()

# Calculate the initial energy and bond length
energy_initial = h2.get_potential_energy()
bond_length_initial = h2.get_distance(0, 1)

# Apply FixBondLength constraint to fix the bond length at 0.9 angstroms
constraint = FixBondLength(0, 1, 0.9)
h2.set_constraint(constraint)

# Calculate the energy and bond length after applying the constraint
energy_constrained = h2.get_potential_energy()
bond_length_constrained = h2.get_distance(0, 1)

# Print the results
print(f'Initial Bond Length: {bond_length_initial:.2f} Å | Initial Energy: {energy_initial:.2f} eV')
print(f'Constrained Bond Length: {bond_length_constrained:.2f} Å | Constrained Energy: {energy_constrained:.2f} eV')
