from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

# Base slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
slab.set_constraint(FixAtoms(mask=[a.tag >= 2 for a in slab]))

# OH molecule
oh = molecule('OH')

# Sites: ontop, bridge, fcc
sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    atoms = slab.copy()
    add_adsorbate(atoms, oh, height=1.8, position=site)
    atoms.calc = EMT()
    energies[site] = atoms.get_potential_energy()

# Find lowest energy site
lowest_site = min(energies, key=energies.get)
print(f"Site energies (eV): {energies}")
print(f"Lowest energy site: {lowest_site} ({energies[lowest_site]:.3f} eV)")
