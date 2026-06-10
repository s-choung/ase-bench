from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

# Create Pt(111) slab
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

# Define OH molecule
oh = Atoms('O', positions=[[0, 0, 0]], cell=slab.cell, pbc=True)

# Function to calculate single-point energy
def calculate_energy(site):
    atoms = slab.copy()
    add_adsorbate(atoms, oh, position=site)
    atoms.center katoms=True
    atoms.calc = EMT()
    return atoms.get_potential_energy()

# Calculate energies for ontop, bridge, and hollow sites
ontop_energy = calculate_energy('ontop')
bridge_energy = calculate_energy('bridge')
fcc_hollow_energy = calculate_energy('fcc-hollow')

# Compare and print results
energies = {'ontop': ontop_energy, 'bridge': bridge_energy, 'fcc_hollow': fcc_hollow_energy}
print("Single-point energies:")
for site, energy in energies.items():
    print(f"{site}: {energy:.4f} eV")

lowest_site = min(energies, key=energies.get)
print(f"\nLowest energy site: {lowest_site} ({energies[lowest_site]:.4f} eV)")
