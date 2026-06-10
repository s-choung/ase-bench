from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixBondLength

h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
h2.calc = EMT()

e_unconstrained = h2.get_potential_energy()
d_unconstrained = h2.get_distance(0, 1)

h2.set_constraint(FixBondLength(0, 1, target=0.9))
opt = BFGS(h2)
opt.run(fmax=0.01)

e_constrained = h2.get_potential_energy()
d_constrained = h2.get_distance(0, 1)

print(f"Without constraint: Bond length = {d_unconstrained:.3f} Å, Energy = {e_unconstrained:.3f} eV")
print(f"With constraint: Bond length = {d_constrained:.3f} Å, Energy = {e_constrained:.3f} eV")
