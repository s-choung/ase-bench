from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# Cu FCC bulk lattice constant optimization using EOS
from ase.eos import Vinet

atoms_bulk = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)
atoms_bulk.calc = EMT()

volumes = []
energies = []
for i in range(1, 7):
    a = i * 0.1
    atoms_bulk.cell = [a, a, a]
    atoms_bulk.positions = atoms_bulk.get_scaled_positions() * a
    volumes.append(atoms_bulk.get_volume())
    energies.append(atoms_bulk.get_potential_energy())

eos = Vinet(volumes, energies)
eos.fit()
lattice_constant = eos.get_bravais_lattice()

# Create (111) slab with 4 layers
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=lattice_constant)
slab.calc = EMT()

# Fix bottom 2 layers
constraint = FixAtoms(indices=[atom.index for atom in slab if atom.position[2] < np.mean(slab.positions[:, 2])])
slab.set_constraint(constraint)

# Relax the slab using BFGS
optimizer = BFGS(slab)
optimizer.run()

# Print final energy and average z-coordinates of each layer
final_energy = slab.get_potential_energy()
z_coords = slab.positions[:, 2]
layer_thickness = slab.cell[2, 2] / 4
avg_z_layer1 = np.mean(z_coords[z_coords < layer_thickness])
avg_z_layer2 = np.mean(z_coords[(z_coords >= layer_thickness) & (z_coords < 2 * layer_thickness)])
avg_z_layer3 = np.mean(z_coords[(z_coords >= 2 * layer_thickness) & (z_coords < 3 * layer_thickness)])
avg_z_layer4 = np.mean(z_coords[z_coords >= 3 * layer_thickness])

print(f"Final Energy: {final_energy:.4f} eV")
print(f"Average z-coordinate of Layer 1: {avg_z_layer1:.4f} Å")
print(f"Average z-coordinate of Layer 2: {avg_z_layer2:.4f} Å")
print(f"Average z-coordinate of Layer 3: {avg_z_layer3:.4f} Å")
print(f"Average z-coordinate of Layer 4: {avg_z_layer4:.4f} Å")
