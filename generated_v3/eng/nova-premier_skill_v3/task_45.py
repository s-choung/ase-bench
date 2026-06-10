from ase import Atoms, units
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLengths

h = molecule('H2')
h.set_calculator(EMT())
print(f"Before: {h.get_distance(0,1):.2f} Å, {h.get_potential_energy():.3f} eV")

h.set_constraint(FixBondLengths([[0,1]], [0.9]))
dyn = BFGS(h)
dyn.run(steps=10)
print(f"After: {h.get_distance(0,1):.2f} Å, {h.get_potential_energy():.3f} eV")
