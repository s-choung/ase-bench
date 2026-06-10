from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create initial H2 molecule with bond length 0.74 Å
atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
atoms.calc = EMT()

# Calculate and print initial values
initial_bond = atoms.get_distance(0, 1)
initial_energy = atoms.get_total_energy()
print(f"Before constraint: Bond length = {initial_bond:.4f} Å, Energy = {initial_energy:.4f} eV")

# Apply FixBondLength constraint to fix at 0.9 Å
atoms.set_constraint(FixBondLength(0, 1, bond_length=0.9))

# Calculate and print final values
final_bond = atoms.get_distance(0, 1)
final_energy = atoms.get_total_energy()
print(f"After constraint: Bond length = {final_bond:.4f} Å, Energy = {final_energy:.4f} eV")
