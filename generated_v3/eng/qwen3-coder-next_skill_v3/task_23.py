from ase import Atoms
from ase.build import fcc111
from ase.molecule import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase import units

# Create Pt(111) 3-layer slab with vacuum
slab = fcc111('Pt', size=(3, 3, 3), vacuum=15.0)
slab.set_calculator(EMT())

# Define adsorbate
oh = molecule('OH')

# Fix bottom two layers
mask = [a.tag <= 1 for a in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Sites: ontop (1 layer up), bridge (between 2 atoms), fcc (3-fold hollow)
# For fcc111, positions are relative to unit cell
positions = {
    'ontop': [1.0, 1.0, 3.0],  # z = 3rd layer height
    'bridge': [0.5, 0.5, 3.0],
    'fcc': [0.5, 0.5, 3.0]  # Will be shifted to fcc hollow in loop
}

energies = {}

for site in ['ontop', 'bridge', 'fcc']:
    # Create copy of slab + OH
    slab_ads = slab.copy()
    
    if site == 'fcc':
        #fcc hollow is at (1/3, 1/3) in fractional coords (or equivalent)
        #Convert to Cartesian and add height above surface
        cell = slab.get_cell()
        frac_pos = [1/3, 1/3, 0]
        cart_pos = cell.dot(frac_pos)
        # Add OH at FCC hollow site with height
        oh_pos = cart_pos + [0, 0, 2.0]  # Height 2.0 Å
        oh.set_positions([oh_pos])
        slab_ads.extend(oh)
    else:
        # Get surface atom position for ontop/bridge
        surface_atom_idx = len(slab) - 1  # Top layer atom
        surface_pos = slab.get_positions()[-1]
        
        if site == 'ontop':
            oh_pos = surface_pos + [0, 0, 2.0]  # Height 2.0 Å above atom
        elif site == 'bridge':
            # Bridge between two atoms: avg of two adjacent top-layer atoms
            atom1 = slab.get_positions()[-1]
            atom2 = slab.get_positions()[-4]  # Next nearest in 3x3 slab
            bridge_pos = (atom1 + atom2) / 2
            oh_pos = bridge_pos + [0, 0, 2.0]  # Height 2.0 Å above bridge
        
        oh.set_positions([oh_pos])
        slab_ads.extend(oh)
    
    # Attach EMT calculator
    slab_ads.calc = EMT()
    
    # Single-point energy
    energy = slab_ads.get_potential_energy()
    energies[site] = energy
    print(f'{site} site energy: {energy:.4f} eV')

# Find minimum energy site
min_site = min(energies, key=energies.get)
print(f"\nLowest energy site: {min_site} ({energies[min_site]:.4f} eV)")
