from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase import units

atoms = Atoms('H2', positions=[[0,0,0],[0.74,0,0]])
atoms.calc = EMT()

print('Before:', atoms.get_distance(0,1), atoms.get_potential_energy())

atoms.set_constraint(FixBondLength(0,1,0.9))
atoms.set_positions([[0,0,0],[0.9,0,0]])

print('After: ', atoms.get_distance(0,1), atoms.get_potential_energy())
