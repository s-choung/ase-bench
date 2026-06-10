from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Setup H2 molecule
h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.7]])
h2.calc = EMT()

# Before constraint
e_before = h2.get_potential_energy()
d_before = h2.get_distance(0, 1)

# Apply FixBondLength constraint (0.9 Angstroms)
constraint = FixBondLength(0, 1, 0.9)
h2.set_constraints(constraint)

# After constraint (Force atoms to the constrained position)
h2.set_positions([[0, 0, 0], [0, 0, 0.9]])
e_after = h2.get_potential_energy()
d_after = h2.get_distance(0, 1)

print(f"Before: Bond={d_before:.3f} A, Energy={e_before:.4f} eV")
print(f"After:  Bond={d_after:.3f} A, Energy={e_after:.4f} eV")
