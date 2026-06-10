from ase import Atoms
from ase.calculators.emt import EMT
from ase.io import write
from ase.data import chemical_symbols
import ase.db

# Function to create a bulk structure for a given element
def create_bulk(element, lattice_constant=4.0):
    symbol = chemical_symbols[element]
    fcc_latt = 4.0 * [[0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]] * lattice_constant
    return Atoms(symbol=symbol, cell=fcc_latt, pbc=True, cellpar=[4.0, 4.0, 4.0, 90, 90, 90])

# Connect to a new ASE database
db = ase.db.connect('bulk_energies.db')

# Create and calculate energies for Cu, Ag, Au bulk structures
for element in ['Cu', 'Ag', 'Au']:
    bulk = create_bulk(element)
    bulk.set_calculator(EMT())
    energy = bulk.get_potential_energy()
    entry = db.new_row()
    entry.formula = element
    entry.energy = energy
    entry.system = bulk

# Query all entries and print formula and energy
for entry in db.select():
    print(f"Element: {entry.formula}, Energy: {entry.energy:.3f} eV")

# Close the database connection
db.close()
