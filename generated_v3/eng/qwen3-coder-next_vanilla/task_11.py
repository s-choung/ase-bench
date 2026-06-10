from ase.build import bulk
from ase import Atoms

# Create BCC Al structure with lattice constant 3.3 Å
al_bcc = bulk('Al', 'bcc', a=3.3, cubic=True)

# Print cell and chemical formula
print("Unit cell:")
print(al_bcc.cell)
print("\nChemical formula:", al_bcc.get_chemical_formula())
