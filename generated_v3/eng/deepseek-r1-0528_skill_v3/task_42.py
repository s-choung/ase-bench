from ase import atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create database and store structures
db = connect('bulk_metals.db')
metals = {
    'Cu': {'a': 3.615, 'crystalstructure': 'fcc'}, 
    'Ag': {'a': 4.085, 'crystalstructure': 'fcc'},
    'Au': {'a': 4.078, 'crystalstructure': 'fcc'}
}

for elem, params in metals.items():
    atoms_obj = bulk(elem, **params)
    atoms_obj.calc = EMT()
    energy = atoms_obj.get_potential_energy()
    db.write(atoms_obj, element=elem, energy=energy)

# Query and print data
print("Database contents:")
with connect('bulk_metals.db') as db:
    for row in db.select():
        print(f"{row.formula}: energy = {row.energy:.6f} eV")
