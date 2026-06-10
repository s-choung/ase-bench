from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create a bulk structure
def create_bulk_structure(element, latticeconstant):
    return bulk(
        element, 
        a=latticeconstant, 
        cubic=True, 
        size=(10, 10, 10)
    )

# Create structures
cu_bulk = create_bulk_structure('Cu', 3.61)
ag_bulk = create_bulk_structure('Ag', 4.09)
au_bulk = create_bulk_structure('Au', 4.07)

# Assign EMT calculator to each structure
cu_bulk.set_calculator(EMT())
cu_bulk.get_potential_energy()

ag_bulk.set_calculator(EMT())
ag_bulk.get_potential_energy()

au_bulk.set_calculator(EMT())
au_bulk.get_potential_energy()

# Connect to a MySQL-like database with ASE's connect function and store the structures
db_file = "unit_test.db"
with connect(db_file) as db:
    cu_bulk_entry = db.create(Bulk)
    cu_bulk_entry.insert_if_missing(cu_bulk)

    ag_bulk_entry = db.create(Bulk)
    ag_bulk_entry.insert_if_missing(ag_bulk)

    au_bulk_entry = db.create(Bulk)
    au_bulk_entry.insert_if_missing(au_bulk)

    # Query all entries from the database
    entries = db.select(Bulk)

    # Print the formula and energy of each entry
    for entry in entries:
        formula = entry.attributes['atom_label']
        energy = entry.calculation['energy']
        print(f"Formula: {formula}, Energy: {energy:.2f}")
