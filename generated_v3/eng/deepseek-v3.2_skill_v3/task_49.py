import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Find equilibrium lattice constant using EOS
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(atoms.cell * x, scale_atoms=True)
    a.calc = EMT()
    energies.append(a.get_potential_energy())
    volumes.append(a.get_volume())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (4 * v0)**(1/3)

# Create slab with optimized lattice constant
slab = fcc111('Cu', size=(2, 2, 4), a=a0, vacuum=10.0)

# Fix bottom 2 layers
mask = [atom.tag < 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Attach calculator and relax
slab.calc = EMT()
opt = BFGS(slab, trajectory='slab_relax.traj')
opt.run(fmax=0.05)

# Print results
print(f"Optimized lattice constant: {a0:.4f} Å")
print(f"Final energy: {slab.get_potential_energy():.4f} eV")

# Calculate average z-coordinate for each layer
layer_zs = {}
for atom in slab:
    tag = atom.tag
    if tag not in layer_zs:
        layer_zs[tag] = []
    layer_zs[tag].append(atom.position[2])

for tag in sorted(layer_zs.keys()):
    avg_z = np.mean(layer_zs[tag])
    print(f"Layer {tag}: average z = {avg_z:.4f} Å")
