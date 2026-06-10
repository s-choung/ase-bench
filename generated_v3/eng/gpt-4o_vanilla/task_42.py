from ase import Atoms
from ase.calculators.emt import EMT
from ase.db import connect

# Define bulk structures
structures = [Atoms('Cu', positions=[(0, 0, 0)], cell=[2, 2, 2], pbc=True),
              Atoms('Ag', positions=[(0, 0, 0)], cell=[2, 2, 2], pbc=True),
              Atoms('Au', positions=[(0, 0, 0)], cell=[2, 2, 2], pbc=True)]

# Create database
with connect('bulk_structures.db') as db:
    for structure in structures:
        structure.calc = EMT()
        energy = structure.get_potential_energy()
        db.write(structure, energy=energy)

# Query and print entries
with connect('bulk_structures.db') as db:
    for row in db.select():
        print(f"Formula: {row.formula}, Energy: {row.data.energy:.2f} eV")
