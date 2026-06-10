from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
import numpy as np

def make_slab():
    slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
    return slab

def get_site_positions(slab):
    cell = slab.get_cell()
    a1 = cell[0]
    a2 = cell[1]
    
    top_layer_z = max(slab.positions[:, 2])
    top_atoms = [atom for atom in slab if abs(atom.position[2] - top_layer_z) < 0.5]
    
    top_positions = np.array([atom.position for atom in top_atoms])
    
    ontop_pos = top_positions[0][:2]
    
    bridge_pos = (top_positions[0][:2] + top_positions[1][:2]) / 2
    
    fcc_pos = (top_positions[0][:2] + top_positions[1][:2] + top_positions[2][:2]) / 3
    
    return ontop_pos, bridge_pos, fcc_pos

sites = ['ontop', 'bridge', 'fcc']
heights = {'ontop': 2.0, 'bridge': 1.8, 'fcc': 1.5}

energies = {}

for site in sites:
    slab = make_slab()
    
    oh = Atoms('OH', positions=[[0, 0, 0], [0, 0, 0.97]])
    
    add_adsorbate(slab, oh, height=heights[site], position=site)
    
    slab.calc = EMT()
    
    energy = slab.get_potential_energy()
    energies[site] = energy
    print(f"Site: {site:10s} | Energy: {energy:.4f} eV")

print("\n--- Results ---")
for site, energy in energies.items():
    print(f"  {site:10s}: {energy:.4f} eV")

best_site = min(energies, key=energies.get)
print(f"\nMost stable adsorption site: {best_site} ({energies[best_site]:.4f} eV)")

print("\nRelative energies (vs most stable):")
for site, energy in energies.items():
    rel = energy - energies[best_site]
    print(f"  {site:10s}: +{rel:.4f} eV")
