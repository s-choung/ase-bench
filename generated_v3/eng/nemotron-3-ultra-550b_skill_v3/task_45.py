from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
atoms.calc = EMT()

bond_len = atoms.get_distance(0, 1)
energy = atoms.get_potential_energy()
print(f"Before constraint: bond={bond_len:.3f} Å, energy={energy:.6f} eV")

constraint = FixBondLength(0, 1, 0.9)
atoms.set_constraint(constraint)

bond_len = atoms.get_distance(0, 1)
energy = atoms.get_potential_energy()
print(f"After constraint:  bond={bond_len:.3f} Å, energy={energy:.6f} eV")
