from ase import Atoms
from ase.db import connect
from ase.build import molecule
from ase.calculators.emt import EMT
from ase import units
from ase.calculations.calculator import Property

# Read CH4 molecule from G2 database
atoms = molecule('CH4')

# Set EMT calculator (for demonstration purposes)
atoms.calc = EMT()

# Optimize geometry to get accurate bond lengths
opt = BFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.05)

# Print atomic coordinates
print("Atomic coordinates (Angstroms):")
for atom in atoms:
    print(f"{atom.symbol:<2}  {atom.position[0]:.3f}  {atom.position[1]:.3f}  {atom.position[2]:.3f}")

# Print bond lengths
print("\nBond lengths (Angstroms):")
for i, atom in enumerate(atoms):
    if atom.symbol == 'C':
        c = atom
        for j, atom_b in enumerate(atoms):
            if i != j and atom_b.symbol == 'H':
                h = atom_b
                print(f"C-H bond length: {(atoms.get_distance(c, h) * units.angstrom):.3f} Å")

# Print chemical formula
print("\nChemical formula:", atoms.get_chemical_formula())
