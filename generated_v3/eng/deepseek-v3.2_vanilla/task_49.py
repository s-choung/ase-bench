from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# Bulk calculation with EOS
bulk_cu = bulk('Cu', 'fcc', a=3.6)
bulk_cu.calc = EMT()
from ase.eos import EquationOfState
volumes = []
energies = []
for factor in np.linspace(0.98, 1.02, 5):
    cell = bulk_cu.cell.copy()
    cell *= factor ** (1/3)
    bulk_cu.set_cell(cell, scale_atoms=True)
    energies.append(bulk_cu.get_potential_energy())
    volumes.append(bulk_cu.get_volume())
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (v0 * 4) ** (1/3)

# Create slab with equilibrium lattice constant
slab = fcc111('Cu', (4, 4, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

# Fix bottom two layers
bottom_indices = [i for i, atom in enumerate(slab) if atom.position[2] < slab[0].position[2] + 2.0 * a0 / np.sqrt(6)]
slab.set_constraint(FixAtoms(indices=bottom_indices))

# Relax surface
opt = BFGS(slab)
opt.run(fmax=0.05)

# Print results
print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Final energy: {slab.get_potential_energy():.6f} eV")
z_positions = slab.positions[:, 2]
layers = np.linspace(z_positions.min(), z_positions.max(), 4)
for i in range(3):
    layer_atoms = np.where((z_positions >= layers[i]) & (z_positions < layers[i+1]))[0]
    avg_z = z_positions[layer_atoms].mean()
    print(f"Layer {i+1} average z: {avg_z:.4f} Å")
