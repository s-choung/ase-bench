from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = Atoms('H2', positions=[[0, 0, ;
atom = Atoms('H2', positions=[[0, 0, 0], [1.0, 0, 0]])
atom.calc = EMT()
energy_initial = atom.get_potential_energy()
distance_initial = atom.get_distance(0, 1)

print(f"Before constraint: bond length = {distance_initial:.3f} Å, energy = {energy_initial:.3f} eV")

constraint = FixBondLength(0, 1)
atom.set_constraint(constraint)
atom.positions[1] = [0.9, 0, 0]

energy_constrained = atom.get_potential_energy()
distance_constrained = atom.get_distance(0, 1)

print(f"After constraint:  bond length = {distance_constrained:.3f} Å, energy = {energy_constrained:.3f} eV")
