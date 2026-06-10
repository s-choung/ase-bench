from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

def find_lowest_energy_site():
    # Build the Pt(111) slab
    slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

    # Coordinates of the OH molecule
    oh = Atoms('OH', positions=[[0, 0, 0], [0, 0, 1.0]])

    # Attach EMT calculator to slab
    slab.set_calculator(EMT())

    # Define adsorption sites
    sites = {
        'ontop': (2 / 3, 1 / 3, 2.0),
        'bridge': (1 / 3, 0, 2.0),
        'fcc': (0.5, 0.5, 2.0)
    }

    energies = {}
    for site_name, pos in sites.items():
        adsorbed_slab = add_adsorbate(slab.copy(), oh, height=pos[2], position=pos[:2])
        adsorbed_slab.set_calculator(EMT())
        energy = adsorbed_slab.get_potential_energy()
        energies[site_name] = energy

    # Find and print the site with the lowest energy
    lowest_site = min(energies, key=energies.get)
    print(f"Site with lowest energy: {lowest_site} ({energies[lowest_site]:.5f} eV)")

# Run the function
find_lowest_energy_site()
