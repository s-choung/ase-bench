from ase import Atoms
from ase.calculators import EMT
from ase.constraints import FixAtoms
from ase.build import molecule

c = molecule('H2')
c.set_constraint(FixAtoms(indices=[0, 1]))
print("Bond length before constraint:", c.get_distance(0, 1))
print("Energy before constraint:", c.get_potential_energy())
c.calc = EMT()
c.get_potential_energy()
print("Bond length after constraint:", c.get_distance(0, 1))
print("Energy after constraint:", c.get_potential_energy())
