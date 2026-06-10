from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

# Create/overwrite database
db = connect('metal_bulks.db', append=False)

# Store Cu, Ag, Au bulk structures with EMT energies
metals = [('Cu', 3.615), ('Ag', 4.086), ('Au', 4.078)]
for symbol, lattice_const in metals:
    atoms = bulk(symbol, 'fcc', a=lattice_const)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

# Query and print all entries
for entry in db.select():
    print(f"Formula: {entry.formula}, Energy: {entry.energy:.4f} eV")
