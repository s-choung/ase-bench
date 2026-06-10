from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create H2 molecule with initial bond length
atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.7]])

# Calculate before constraint
atoms.calc = EMT()
e_before = atoms.get_potential_energy()
d_before = atoms.get_distance(0, 1)

# Apply constraint to fix bond at 0.9 Å
atoms.set_distance(0, 1, 0.9)
constraint = FixBondLength(0, 1)
atoms.set_constraint(constraint)

# Calculate after constraint
e_after = atoms.get_potential_energy()
d_after = atoms.get_distance(0, 1)

print(f"Before constraint: Bond length = {d_before:.3f} Å, Energy = {e_before:.3f} eV")
print(f"After constraint: Bond length = {d_after:.3f} Å, Energy = {e_after:.3f} eV")
