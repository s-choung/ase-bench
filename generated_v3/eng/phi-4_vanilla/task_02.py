from ase.build import bulk, surface, add_adsorbate
from ase.build import fcc111

# Create a Pt(111) 4-layer slab with 10 angstroms of vacuum
pbs = fcc111('Pt', layers=4, a=3.92, vacuum=10)

# Add a carbon monoxide (CO) molecule on the atop site
co = add_adsorbate(pbs, 'CO', site=1)

# Print the number of atoms in the final structure
print(f"Number of atoms in the slab: {len(pbs)}")
print(f"Number of atoms in CO: {len(co)}")
print(f"Total number of atoms in the slab: {len(pbs) + len(co)}")
