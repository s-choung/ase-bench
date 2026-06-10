from ase.build import fcc111, molecule
from ase.visualize import view
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

def get_adsorption_energy(site):
    # Build Pt(111) slab: 3 layers, 10A vacuum
    slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
    
    # Define adsorption positions (relative to surface Pt atoms)
    # Positions for a 3x3 unit cell based on fcc111 lattice
    positions = {
        'ontop':  (0.0, 0.0, 2.0),
        'bridge': (0.5, 0.0, 2.0),
        'fcc':    (0.333, 0.333, 2.0)
    }
    
    # Prepare OH molecule
    oh = molecule('OH')
    # Rotate/Orient OH if necessary (simplified here as a vector)
    oh.rotate(90, 'x')
    
    # Add adsorbate to slab
    from ase.build import add_adsorbate
    # Note: add_adsorbate is in-place; we use a copy to keep slab clean
    test_slab = slab.copy()
    add_adsorbate(test_slab, oh, height=2.0, position=site)
    
    # Fix slab atoms (indices 0 to 8 are the 3 layers of Pt)
    test_slab.set_constraint(FixAtoms(indices=range(len(slab))))
    
    # Calculate Energy
    test_slab.calc = EMT()
    return test_slab.get_potential_energy()

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for s in sites:
    try:
        # EMT only supports Cu, Ag, Au, Ni, Pd, Pt, Al. Pt is supported.
        # Note: EMT is a simple empirical potential, results are for demonstration.
        energies[s] = get_adsorption_energy(s)
        print(f"Site: {s:6} | Energy: {energies[s]:.4f} eV")
    except Exception as e:
        print(f"Error at {s}: {e}")

best_site = min(energies, key=energies.get)
print(f"\nLowest energy site: {best_site} ({energies[best_site]:.4f} eV)")
