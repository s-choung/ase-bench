from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import fcc111

# Create Pt(111) 3-layer slab (2x2 unit cells)
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Store slab copies for each adsorption site
structures = {'ontop': slab.copy(), 'bridge': slab.copy(), 'fcc': slab.copy()}

# Get surface atom coordinates for reference
surface_atoms = [atom.index for atom in slab if atom.tag == 0]  # top layer atoms

# Define adsorption height and OH bond length
ads_height = 1.8
oh_bond = 0.97

# On-top site: above first surface atom
pos = slab.positions[surface_atoms[0]].copy()
pos[2] += ads_height
structures['ontop'].extend(Atoms('OH', positions=[[pos[0], pos[1], pos[2]], 
                                                 [pos[0], pos[1], pos[2] + oh_bond]]))

# Bridge site: midpoint between two adjacent surface atoms
pos1 = slab.positions[surface_atoms[0]].copy()
pos2 = slab.positions[surface_atoms[1]].copy()
mid = (pos1 + pos2) / 2
mid[2] += ads_height
structures['bridge'].extend(Atoms('OH', positions=[[mid[0], mid[1], mid[2]], 
                                                   [mid[0], mid[1], mid[2] + oh_bond]]))

# Fcc hollow site: center of three adjacent surface atoms (first hollow)
pos1 = slab.positions[surface_atoms[0]].copy()
pos2 = slab.positions[surface_atoms[1]].copy()
pos3 = slab.positions[surface_atoms[2]].copy()
fcc_pos = (pos1 + pos2 + pos3) / 3
fcc_pos[2] += ads_height
structures['fcc'].extend(Atoms('OH', positions=[[fcc_pos[0], fcc_pos[1], fcc_pos[2]], 
                                               [fcc_pos[0], fcc_pos[1], fcc_pos[2] + oh_bond]]))

# Compute energies
energies = {}
calculator = EMT()
for site, atoms in structures.items():
    atoms.calc = calculator
    energies[site] = atoms.get_potential_energy()

# Find lowest energy site
min_site = min(energies, key=energies.get)
print("Energies (eV):")
for site, energy in energies.items():
    print(f"{site}: {energy:.4f}")
print(f"\nLowest energy site: {min_site} ({energies[min_site]:.4f} eV)")
