from ase.build import fcc111
from ase.io import write
from ase import Atoms
from ase.calculators.emt import EMT
import numpy as np

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
slab.calc = EMT()

# Adsorb OH on top
oh = Atoms(['O', 'H'],
           positions=[[0.0, 0.0, 0.0], [0.0, 0.0, 0.9]])
oh_top = slab + oh
oh_top.set_constraint(FixAtoms(mask=[True] + [False] * (len(oh_top) - 1)))
energy_top = oh_top.get_potential_energy()

# Adsorb OH on bridge
oh_bridge = slab + oh
oh_bridge.positions[1] = [0.75, 0.75, 0.9]
oh_bridge.set_constraint(FixAtoms(mask=[True] + [False] * (len(oh_bridge) - 1)))
energy_bridge = oh_bridge.get_potential_energy()

# Adsorb OH on fcc hollow
oh_hollow = slab + oh
oh_hollow.positions[1] = [0.5, 0.5, 0.9]
oh_hollow.set_constraint(FixAtoms(mask=[True] + [False] * (len(oh_hollow) - 1)))
energy_hollow = oh_hollow.get_potential_energy()


energies = {
    'ontop': energy_top,
    'bridge': energy_bridge,
    'hollow': energy_hollow,
}

best_site = min(energies, key=energies.get)
lowest_energy = energies[best_site]

print(f"Energy ontop: {energy_top:.3f} eV")
print(f"Energy onbridge: {energy_bridge:.3f} eV")
print(f"Energy onhollow: {energy_hollow:.3f} eV")

print(f"Lowest energy: {lowest_energy:.3f} eV at {best_site} site")
