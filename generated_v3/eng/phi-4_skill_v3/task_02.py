from ase.build import bulk, add_adsorbate, fcc111
from ase import Atoms

# Create a 4-layer Pt(111) slab with 2x2 surface unit cells and 10 angstroms of vacuum
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10)

# Create a CO molecule
co = Atoms('CO')

# Add the CO molecule on the ontop site of the slab
add_adsorbate(slab, co, height=1.5, position='ontop')

# Print the number of atoms in the final structure
print("Number of atoms in the final structure:", len(slab))

# Example output structure for debugging
# slab.write('ptslab.xyz')  # Uncomment to write the structure to a file for visualization
