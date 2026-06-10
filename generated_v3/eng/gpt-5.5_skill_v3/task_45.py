from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = Atoms("H2", positions=[[0, 0, 0], [0, 0, 0.74]])
h2.calc = EMT()

print(f"Before constraint: bond length = {h2.get_distance(0, 1):.3f} Å")
print(f"Before constraint: energy = {h2.get_potential_energy():.6f} eV")

h2.set_distance(0, 1, 0.9)
h2.set_constraint(FixBondLength(0, 1))

print(f"After constraint: bond length = {h2.get_distance(0, 1):.3f} Å")
print(f"After constraint: energy = {h2.get_potential_energy():.6f} eV")
