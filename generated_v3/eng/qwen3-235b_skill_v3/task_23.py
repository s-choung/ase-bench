from ase import Atoms
from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
from ase.io import read, write

# Create Pt(111) 3-layer slab with vacuum
slab = fcc111('Pt', size=(1,1,3), vacuum=10.0)

# Create OH molecule
oh = molecule('OH')
oh.rotate(90, 'x')  # Rotate to stand upright

sites = ['ontop', 'bridge', 'fcc']
energies = []

for site in sites:
    # Copy pristine slab
    atoms = slab.copy()
    # Add OH at given site
    add_adsorbate(atoms, oh, height=1.0, position=site)
    # Attach EMT calculator
    atoms.calc = EMT()
    # Compute and store energy
    energy = atoms.get_potential_energy()
    energies.append(energy)

# Find most stable site
best_site = sites[energies.index(min(energies))]
print(f"Lowest energy site: {best_site}")
