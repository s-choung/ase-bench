from ase.build import molecule
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

# Create H2 and set target bond length (0.9 Å)
h2 = molecule('H2')
h2.positions[1] = [0.9, 0.0, 0.0]

# Initial state (no constraint)
h2.calc = EMT()
init_bond = h2.get_distance(0, 1)
init_energy = h2.get_potential_energy()
print(f'Before constraint: Bond={init_bond:.2f}Å, Energy={init_energy:.4f}eV')

# Apply fixed bond length constraint
h2.set_constraint(FixBondLength(0, 1))

# Final state (with constraint)
fin_bond = h2.get_distance(0, 1)
fin_energy = h2.get_potential_energy()
print(f'After constraint: Bond={fin_bond:.2f}Å, Energy={fin_energy:.4f}eV')
