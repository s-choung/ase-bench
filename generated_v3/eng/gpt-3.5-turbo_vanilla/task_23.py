from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
oh = Atoms('OH', positions=[(0, 0, 0)])
energies = {}

sites = ['ontop', 'bridge', 'fcc']
for site in sites:
    slab_copy = slab.copy()
    add_adsorbate(slab_copy, oh, 1.7, site)
    
    slab_copy.set_calculator(EMT())
    energy = slab_copy.get_potential_energy()
    
    energies[site] = energy

lowest_energy_site = min(energies, key=energies.get)
print(f'{lowest_energy_site} site has the lowest energy: {energies[lowest_energy_site]} eV')
