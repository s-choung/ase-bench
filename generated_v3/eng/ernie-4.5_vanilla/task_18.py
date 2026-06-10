from ase.build import molecule
from ase.calculators.emt import EMT
from ase.geometry.analysis import Analysis
from ase.formulas import chemical_formula

# Retrieve CH4 molecule from the ASE G2 database (manually defined since G2 extraction isn't direct)
# Alternatively, use ASE's molecule function to build CH4
atoms = molecule('CH4')

# Use EMT calculator to compute energies (and potentially forces, but not required here)
atoms.set_calculator(EMT())

# Print atomic coordinates
print("Atomic Coordinates:")
for atom in atoms:
    print(f"{atom.symbol}: {atom.position[:]} Å")

# Compute bond lengths using Analysis
analysis = Analysis(atoms)
bond_list = analysis.get_bonds(radius=1.2)  # Using a generic radius for C-H bonds

print("\nBond Lengths:")
for i, (a1, a2, dist) in enumerate(bond_list):
    print(f"Bond {i + 1}: {atoms[a1].symbol}-{atoms[a2].symbol} = {dist:.4f} Å")

# Print chemical formula
formula = chemical_formula(atoms.get_chemical_symbols())
print(f"\nChemical Formula: {formula}")
