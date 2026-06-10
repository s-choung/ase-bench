from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
atoms.calc = EMT()
print(atoms.get_distance(0, 1), atoms.get_potential_energy())
atoms.set_distance(0, 1, 0.9)
atoms.set_constraint(FixBondLength(0, 1))
print(atoms.get_distance(0, 1), atoms.get_potential_energy())
