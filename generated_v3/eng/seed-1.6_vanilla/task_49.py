from ase.atoms import Atoms
from ase.build import bulk, surface
from ase.eos import EOS
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Find equilibrium FCC Cu lattice constant via EOS
bulk_cu = bulk('Cu', 'fcc')
bulk_cu.calc = EMT()
eos = EOS(bulk_cu)
v0, _, _ = eos.fit()
a0 = v0 ** (1/3)

# Create 4-layer (111) slab with equilibrium a0
bulk_eq = bulk('Cu', 'fcc', a=a0)
slab = surface(bulk_eq, (111), layers=4, vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers (tolerance for z-grouping)
tol = 0.1
z_init = slab.positions[:, 2]
unique_z = sorted(list({round(z/tol)*tol for z in z_init}))
for atom in slab:
    if round(atom.z/tol)*tol in unique_z[:2]:
        atom.fix_position(True)

# Relax slab with BFGS
opt = BFGS(slab)
opt.run(fmax=0.01)

# Print final energy
print(f'Final energy: {slab.get_potential_energy():.6f} eV')

# Print average z per layer (post-relaxation)
z_relax = slab.positions[:, 2]
layers = {}
for z in z_relax:
    key = round(z/tol)*tol
    layers.setdefault(key, []).append(z)
sorted_layers = sorted(layers.items(), key=lambda x: x[0])
for i, (_, zs) in enumerate(sorted_layers, 1):
    avg_z = sum(zs)/len(zs)
    print(f'Layer {i} avg z: {avg_z:.3f} Å')
