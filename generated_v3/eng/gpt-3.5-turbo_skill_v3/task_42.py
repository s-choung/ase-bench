from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

# Connect to the ASE database
db = connect('bulk_metals.db')

# Define the elements and create bulk structures
elements = ['Cu', 'Ag', 'Au']
for element in elements:
    atoms = bulk(element, crystalstructure='fcc', a=4.0)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    
    # Store the structure and energy in the database
    db.write(atoms, energy=energy, formula=element+'_bulk')

# Query all entries in the database and print the formula and energy
for row in db.select():
    formula = row.formula
    energy = row.energy
    print(f'Formula: {formula}, Energy: {energy:.2f} eV')
