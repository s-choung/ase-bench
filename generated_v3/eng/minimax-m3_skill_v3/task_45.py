from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.75]])
atoms.calc = EMT()

d0 = atoms.get_distance(0, 1)
e0 = atoms.get_potential_energy()
print(f"Before constraint: bond={d0:.4f} A, energy={e0:.4f} eV")

atoms.set_constraint(FixBondLength(0, 1, bondlength=0.9))
e1 = atoms.get_potential_energy()
d1 = atoms.get_distance(0, 1)
print(f"After constraint:  bond={d1:.4f} A, energy={e1:.4f} eV")
