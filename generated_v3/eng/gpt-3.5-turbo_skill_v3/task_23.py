from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Initialize EMT calculator
slab.calc = EMT()

# Adsorb OH molecule on ontop, bridge, fcc hollow sites
positions = ['ontop', 'bridge', 'fcc']
energies = []

for pos in positions:
    slab_ads = slab.copy()
    oh = molecule('OH')
    add_adsorbate(slab_ads, oh, height=1.5, position=pos)
    slab_ads.set_constraint(FixAtoms(mask=[a.tag >= 4 for a in slab_ads]))  # Fix slab atoms
    opt = BFGS(slab_ads)
    opt.run(fmax=0.05)
    energies.append(slab_ads.get_potential_energy())

# Compare and print lowest energy site
lowest_energy_site = positions[energies.index(min(energies))]
print(f"The lowest energy site for OH adsorption on Pt(111) is: {lowest_energy_site}")
