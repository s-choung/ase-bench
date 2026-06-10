from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.io import Trajectory
from ase.constraints import FixAtoms

# Create a 3-layer Pt(111) slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
slab.set_constraint(FixAtoms(indices=[atom.index for atom in slab if atom.tag == 1]))

# Positions for OH adsorption
adsorption_sites = {'ontop': (0, 1.0),
                    'bridge': (1, 1.0),
                    'fcc': (2, 1.0)}

# Initialize result dictionary
energies = {}

# Adsorb OH molecule and calculate energies
for site, (index, height) in adsorption_sites.items():
    # Create a copy of the slab for each site
    slab_copy = slab.copy()
    
    # Add OH molecule at the given site
    oh = molecule("OH")
    add_adsorbate(slab_copy, oh, height=height, position=site)
    
    # Attach calculator
    slab_copy.set_calculator(EMT())
    
    # Calculate energy
    energy = slab_copy.get_potential_energy()
    energies[site] = energy

# Find the site with the lowest energy
min_site = min(energies, key=energies.get)
print(f"The site with the lowest energy is {min_site} with an energy of {energies[min_site]:.3f} eV")
