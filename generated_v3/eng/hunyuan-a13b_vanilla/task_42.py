from ase import Atoms
from ase.db import Database
from ase.calculators import EMT

# Define structures
structures = {
    "Cu bulk": Atoms('Cu', cell='fcc', a=3.61, pbc=True),
    "Ag bulk": Atoms('Ag', cell='fcc', a=4.09, pbc=True),
    "Au bulk": Atoms('Au', cell='fcc', a=4.08, pbc=True)
}

# Initialize database
db = Database('materials.db')

# Calculate energies and insert into database
for name, struct in structures.items():
    calc = EMT()
    struct.set_calculator(calc)
    energy = struct.get_total_energy()
    db.write(struct, energy=energy, formula=name)

# Query and print entries
for entry in db.select():
    print(f"Formula: {entry.formula}, Energy: {entry.energy:.6f} eV")
