from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

# Optimize Pt bulk to get lattice constant
pt_bulk = Atoms('Pt', positions=[[0,0,0]], cell=[2.8,2.8,2.8], pbc=True)
pt_bulk.calc = EMT()
pt_bulk.get_potential_energy()
a_opt = pt_bulk.cell[0, 0] * (4 / (3**0.5))**(1/3)

# Build Pt(111) 3-layer slab
slab = fcc111('Pt', size=(3, 3, 3), a=a_opt, vacuum=10.0)
oh = Atoms('OH', positions=[[0, 0, 0], [0.76, 0, 0]])

# Create systems for each adsorption site
sites = ['ontop', 'bridge', 'fcc']
systems = []
for site in sites:
    atoms = slab.copy()
    add_adsorbate(atoms, oh, height=1.2, position=site)
    atoms.calc = EMT()
    systems.append((site, atoms))

# Compute energies
results = []
for site, system in systems:
    energy = system.get_potential_energy()
    results.append((site, energy))

# Find and report most stable site
stable_site = min(results, key=lambda x: x[1])
print(f"Adsorption site energies (eV):")
for site, energy in results:
    print(f"{site}: {energy:.4f}")
print(f"Most stable site: {stable_site[0]} ({stable_site[1]:.4f} eV)")
