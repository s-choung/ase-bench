from ase import Atoms
from ase.calculators.emt import EMT

atoms = Atoms('Cu', positions=[(0, 0, 0), (2.5, 2.5, 0), (-2.5, 2.5, 0), (2.5, -2.5, 0),
                                (-2.5, -2.5, 0), (0, 0, 2.5), (0, 0, -2.5)], cell=(5, 5, 5))

atoms.set_calculator(EMT())
print("Number of atoms:", len(atoms))
print("Positions shape:", atoms.get_positions())
