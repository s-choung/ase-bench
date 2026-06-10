from ase import Atoms
from ase.calculators.emt import EMT
from ase.db import connect
from ase.lattice.cubic import FaceCenteredCubic

# Create database and add structures
db = connect('bulk_energies.db')

# Create bulk structures for Cu, Ag, Au
for symbol in ['Cu', 'Ag', 'Au']:
    # Create bulk structure with 2x2x2 supercell for better representation
    atoms = FaceCenteredCubic(symbol, size=(2, 2, 2), latticeconst=None)
    # Set EMT calculator
    atoms.calc = EMT()
    # Get energy
    energy = atoms.get_total_energy()
    # Add to database with metadata
    db.write(atoms, formula=symbol, name=f'{symbol}_bulk', energy=energy)

# Query all entries and print formula and energy
print("Formula | Energy (eV)")
print("-" * 25)
for row in db.select():
    print(f"{row.formula:7} | {row.energy:.4f}")
