from ase.build import add_adsorbate
from ase.lattice.cubic import FaceCenteredCubic
from ase.io import write, read
from ase.calculators.emt import EMT

# Create NaCl structure (FCC)
atoms = FaceCenteredCubic(
    directions=[1, 0, 0],
    symbol='Na',
    latticeconstant=5.64,
    scale=1
)
# Add Cl atoms to create NaCl structure (shifting Na by 0.5, 0.5, 0.5)
atoms.append(FaceCenteredCubic(
    directions=[1, 0, 0],
    symbol='Cl',
    latticeconstant=5.64,
    scale=1
))
# Offset the Cl lattice to form the NaCl structure
atoms[len(atoms)//2 :].positions += [2.82, 2.82, 2.82]

# Use a built-in calculator
atoms.calc = EMT()

# Save to CIF
write('nacl.cif', atoms, format='cif')

# Read back
loaded_atoms = read('nacl.cif')

# Print requested info
print(f"Number of atoms: {len(loaded_atoms)}")
# ASE does not calculate spacegroups natively without spglib, 
# but we can access the cell/positions
print(f"Cell:\n{loaded_atoms.cell}")
