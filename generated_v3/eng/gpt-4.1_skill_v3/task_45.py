from ase.build import molecule
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

# Build H2 molecule
atoms = molecule('H2')
atoms.calc = EMT()

# Initial bond length and energy
bond_idx = (0, 1)
init_bond = atoms.get_distance(*bond_idx)
init_energy = atoms.get_potential_energy()
print(f'Before constraint: Bond length = {init_bond:.3f} Å, Energy = {init_energy:.6f} eV')

# Fix bond (set to 0.9 Å) and move atoms accordingly
atoms.set_distance(*bond_idx, distance=0.9, fix=0)
atoms.set_constraint(FixBondLength(*bond_idx))

# Recalculate energy
constrained_bond = atoms.get_distance(*bond_idx)
constrained_energy = atoms.get_potential_energy()
print(f'After constraint: Bond length = {constrained_bond:.3f} Å, Energy = {constrained_energy:.6f} eV')
