from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Create and connect to ASE database
db = connect('noble_metals.db')

# Process each bulk metal
for symbol in ['Cu', 'Ag', 'Au']:
    # Build fcc cubic bulk structure
    atoms = bulk(symbol, 'fcc', cubic=True)
    # Assign EMT calculator
    atoms.calc = EMT()
    # Relax cell and atomic positions
    filter = FrechetCellFilter(atoms)
    opt = BFGS(filter)
    opt.run(fmax=0.01)
    # Store structure and energy in database
    db.write(atoms, element=symbol)

# Query all entries and print results
print("\nStored database entries:")
for entry in db.select():
    print(f"Formula: {entry.formula:4s} | EMT Energy: {entry.energy:.3f} eV")
