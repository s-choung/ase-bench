from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.lj import LennardJones
import numpy as np

# Create Pt(111) slab
slab = fcc111('Pt', size=(2, 2, 3), a=3.92)
slab.center(vacuum=10, axis=2)

# Get surface atoms (top layer)
positions = slab.positions
z = positions[:, 2]
surface_index = np.where(z == z.max())[0]
surface_pos = positions[surface_index]

# Compute sites (x, y)
ontop_xy = surface_pos[0, :2]
# For bridge: midpoint of first two surface atoms (should be adjacent)
bridge_xy = (surface_pos[0, :2] + surface_pos[1, :2]) / 2
# For fcc hollow: average of three atoms forming a triangle (first three)
hollow_xy = surface_pos[:3, :2].mean(axis=0)

# OH molecule geometry
bond_length = 0.97
height = z.max() + 2.0  # Pt-O distance

sites = {'ontop': ontop_xy, 'bridge': bridge_xy, 'fcc': hollow_xy}
energies = {}

for name, xy in sites.items():
    # Copy slab
    system = slab.copy()
    # Add OH molecule
    oh = Atoms(['O', 'H'],
               positions=[(xy[0], xy[1], height),
                          (xy[0], xy[1], height + bond_length)])
    system += oh
    # Attach calculator
    system.calc = LennardJones()
    energies[name] = system.get_potential_energy()

# Compare
lowest = min(energies, key=energies.get)
for name, energy in energies.items():
    print(f'{name} site energy: {energy:.4f} eV')
print(f'Lowest energy site: {lowest}')
