from ase.build import fcc111, molecule, add_adsorbate, add_vacuum
from ase.calculators.emt import EMT

# Create Pt(111) 4-layer slab
slab = fcc111('Pt', size=(2, 2, 4), vacuum=0.0)  # Initial vacuum=0
add_vacuum(slab, 10.0)  # Add 10 Å vacuum (in-place modification)

# Create CO molecule
co = molecule('CO')

# Add CO on ontop site (in-place modification)
add_adsorbate(slab, co, height=1.8, position='ontop')

# Optional: Attach EMT calculator (not used in this example)
slab.calc = EMT()

# Print number of atoms
print(f"Number of atoms in final structure: {len(slab)}")
