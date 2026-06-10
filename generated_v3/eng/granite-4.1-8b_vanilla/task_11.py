from ase import Atoms
from ase.calculators.emt import EMT

# Create Al BCC structure with a lattice constant of 3.3 Å
atoms = Atoms('Al', scaledpositions=[[0, 0, 0]],
              cell=[3.3, 3.3, 3.3], cubic=True)

# Assign an EMT calculator (although it's not used for printing)
atoms.set_calculator(EMT())

# Print the cell parameters and chemical formula
print(atoms.cell)
print(atoms.get_chemical_formula())
