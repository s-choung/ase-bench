from ase.build import fcc111, molecule, add_adsorbate

# Create 4-layer Pt(111) slab with 10Å vacuum
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
# Load CO molecule and adsorb on ontop site
co_mol = molecule('CO')
add_adsorbate(slab, co_mol, height=1.8, position='ontop')
# Print total number of atoms
print(f"Total atoms in final structure: {len(slab)}")
