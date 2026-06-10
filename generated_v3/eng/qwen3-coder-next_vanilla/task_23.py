from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

# Create Pt(111) 3-layer slab with 4x4 supercell
slab = fcc111('Pt', size=(4, 4, 3), vacuum=10.0)

# Fix bottom 2 layers
fix_mask = [atom.z < 2 * slab.cell[2, 2] / 3 for atom in slab]
constraint = FixAtoms(mask=fix_mask)
slab.set_constraint(constraint)

# Define adsorption sites (fractional coordinates relative to slab cell)
# Top site: above a surface atom
top_site = [0.0, 0.0, 2.5]

# Bridge site: between two adjacent surface atoms
bridge_site = [0.5, 0.0, 2.0]

#fcc hollow site: centered over fcc hollow
fcc_hollow_site = [0.5, 0.5, 2.0]

# Create OH adsorbate (O at origin, H at 0.96 Å along z)
oh = Atoms('OH', positions=[[0.0, 0.0, 0.0], [0.0, 0.0, 0.96]])

# Create structures for each site
structures = []

# Top site
top_slab = slab.copy()
top_oh = oh.copy()
top_oh.translate(top_site)
top_slab.extend(top_oh)
top_slab.calc = EMT()
top_energy = top_slab.get_potential_energy()
structures.append(('top', top_energy))

# Bridge site
bridge_slab = slab.copy()
bridge_oh = oh.copy()
bridge_oh.translate(bridge_site)
bridge_slab.extend(bridge_oh)
bridge_slab.calc = EMT()
bridge_energy = bridge_slab.get_potential_energy()
structures.append(('bridge', bridge_energy))

# fcc hollow site
fcc_slab = slab.copy()
fcc_oh = oh.copy()
fcc_oh.translate(fcc_hollow_site)
fcc_slab.extend(fcc_oh)
fcc_slab.calc = EMT()
fcc_energy = fcc_slab.get_potential_energy()
structures.append(('fcc', fcc_energy))

# Print energies and find minimum
print("Adsorption energies (eV):")
for site, energy in structures:
    print(f"{site}: {energy:.4f}")

min_site = min(structures, key=lambda x: x[1])
print(f"\nLowest energy site: {min_site[0]} ({min_site[1]:.4f} eV)")
