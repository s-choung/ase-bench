from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = Atoms("H2", positions=[(0, 0, 0), (0, 0, 0.74)])
h2.calc = EMT()

print(f"Before constraint: bond length = {h2.get_distance(0, 1):.6f} Å, energy = {h2.get_potential_energy():.6f} eV")

h2.set_distance(0, 1, 0.9, fix=0)
h2.set_constraint(FixBondLength(0, 1))

print(f"After constraint:  bond length = {h2.get_distance(0, 1):.6f} Å, energy = {h2.get_potential_energy():.6f} eV")
