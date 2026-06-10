from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

# Create database and store structures with EMT energies
with connect('metals.db', overwrite=True) as db:
    for symbol, lattice_constant in [('Cu', 3.61), ('Ag', 4.09), ('Au', 4.08)]:
        atoms = bulk(symbol, 'fcc', a=lattice_constant)
        atoms.calc = EMT()
        db.write(atoms, data={'energy': atoms.get_potential_energy()})

# Query and print formula and energy
with connect('metals.db') as db:
    for row in db.select():
        print(f"{row.formula}: {row.data['energy']:.4f} eV")
