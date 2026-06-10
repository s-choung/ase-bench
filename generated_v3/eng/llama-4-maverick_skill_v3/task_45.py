from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.8]])
h2.calc = EMT()

initial_bond_length = h2.get_distance(0, 1)
initial_energy = h2.get_potential_energy()
print(f"Initial bond length: {initial_bond_length:.3f} Å, Initial energy: {initial_energy:.3f} eV")

constraint = FixBondLength(0, 1)
h2.set_constraint(constraint)
h2.positions[1, 2] = 0.9  # manually adjust to demonstrate constraint effect

constrained_bond_length = h2.get_distance(0, 1)
constrained_energy = h2.get_potential_energy()
print(f"Constrained bond length: {constrained_bond_length:.3f} Å, Constrained energy: {constrained_energy:.3f} eV")

# verify the bond length remains fixed during optimization
from ase.optimize import BFGS
opt = BFGS(h2)
opt.run(fmax=0.01)
final_bond_length = h2.get_distance(0, 1)
final_energy = h2.get_potential_energy()
print(f"Final bond length: {final_bond_length:.3f} Å, Final energy: {final_energy:.3f} eV")
