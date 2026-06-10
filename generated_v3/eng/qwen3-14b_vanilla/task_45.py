from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = Atoms('H2', positions=[[0, 0, 0], [0.9, 0, 0]])
h2.set_calculator(EMT())
bl_before = h2.get_distance(0, 1)
e_before = h2.get_potential_energy()
print(f"Before: Bond Length = {bl_before:.2f} Å, Energy = {e_before:.4f} eV")

constraint = FixBondLength(0, 1, 0.9)
h2.set_constraint(constraint)
bl_after = h2.get_distance(0, 1)
e_after = h2.get_potential_energy()
print(f"After: Bond Length = {bl_after:.2f} Å, Energy = {e_after:.4f} eV")
