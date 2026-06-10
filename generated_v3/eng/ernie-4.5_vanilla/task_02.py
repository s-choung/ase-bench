from ase.build import fcc111, add_adsorbate
from ase import Atom, Atoms
from ase.calculators.emt import EMT

# Create a Pt(111) slab with 4 layers
slab = fcc111('Pt', size=(1, 1, 4), vacuum=10.0)

# Add a CO molecule on the ontop site
co = Atoms([Atom('C', (0, 0, 0)), Atom('O', (0, 0, 1.2))], cell=slab.cell)
add_adsorbate(slab, co, 1.9, 'ontop')  # 1.9 Å is an example bond length for Pt-C

# Combine the slab and CO into a single structure
# (add_adsorbate already modifies the slab in-place, so no need to combine explicitly)

# Use EMT calculator (optional, if you want to calculate energy or relax)
slab.set_calculator(EMT())

# Print number of atoms in the final structure
print(f"Number of atoms: {len(slab)}")
