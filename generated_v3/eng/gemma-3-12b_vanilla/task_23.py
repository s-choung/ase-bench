from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.io import write

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
calc = EMT()
slab.calc = calc

oh = ('OH', {'positions': [[0.0, 0.0, 0.0]]})

ontop = slab.copy()
add_adsorbate(ontop, oh, site='ontop')
energy_ontop = ontop.calc.results['energy']

bridge = slab.copy()
add_adsorbate(bridge, oh, site='bridge')
energy_bridge = bridge.calc.results['energy']

fcc_hollow = slab.copy()
add_adsorbate(fcc_hollow, oh, site='fcc')
energy_fcc_hollow = fcc_hollow.calc.results['energy']

energies = {'ontop': energy_ontop, 'bridge': energy_bridge, 'fcc': energy_fcc_hollow}
best_site = min(energies, key=energies.get)

print(f"Ontop energy: {energy_ontop}")
print(f"Bridge energy: {energy_bridge}")
print(f"Fcc hollow energy: {energy_fcc_hollow}")
print(f"Lowest energy at site: {best_site}")
