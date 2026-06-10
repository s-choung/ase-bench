from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
atoms.calc = EMT()

d0 = atoms.get_distance(0, 1)
e0 = atoms.get_potential_energy()
print(f"Before constraint: bond length = {d0:.3f} Å, energy = {e0:.6f} eV")

atoms.set_distance(0, 1, 0.9, fix=0)
atoms.set_constraint(FixBondLength(0, 1))

d1 = atoms.get_distance(0, 1)
e1 = atoms.get_potential_energy()
print(f"After constraint:  bond length = {d1:.3f} Å, energy = {e1:.6f} eV")
