from ase import Atom, Molecule
from ase.build import molecule
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

# Create H2 molecule
h2 = molecule('H2', atoms='H 0 0 0; H 0 0 1.1', cell='0 0 10', pbc=True)
h2.view()

# EMT calculator
calc = EMT()

# Initial calculation
calc Mol.h2
initial_energy = calc.e
bond_length = h2.get_distance(0, 1)
print(f"Initial bond length: {bond_length:.3f} Å, Initial energy: {initial_energy:.3f} eV")

# Apply FixBondLength constraint
bond_indices = [(0, 1)]
constraint = FixBondLength(h2, bond_indices, 0.9)
h2 Isolated constraint
calc;
h2.isolated constraint

# Final calculation
final_energy = calc.e
final_bond_length = h2.get_distance(0, 1)
print(f"Final bond length: {final_bond_length:.3f} Å, Final energy: {final_energy:.3f} eV")

# Clean up
h2 Isolated
