import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
from ase.constraints import FixAtoms

# EOS for bulk Cu
cu_bulk = bulk('Cu', 'fcc', a=3.6)
calc_emt = EMT()
cu_bulk.calc = calc_emt
a0s = np.linspace(3.4, 3.8, 7)
volumes, energies = [], []
for a in a0s:
    cu = cu_bulk.copy()
    cu.set_cell([a, a, a], scale_atoms=True)
    cu.calc = calc_emt
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())
eos = EquationOfState(volumes, energies)
v0, _, _ = eos.fit()
a_eq = v0**(1/3)

# Create 4-layer (111) slab
slab = fcc111('Cu', size=(2,2,4), a=a_eq, vacuum=10.0)
layers = []
z_pos = np.array([atom.z for atom in slab])
zs_unique = np.unique(z_pos.round(decimals=5))
for z in sorted(zs_unique):
    mask = np.isclose(slab.positions[:,2], z, atol=1e-5)
    layers.append(np.where(mask)[0])

slab.calc = EMT()
mask_bottom = [i in layers[0] or i in layers[1] for i in range(len(slab))]
slab.set_constraint(FixAtoms(mask=mask_bottom))
opt = BFGS(slab)
opt.run(fmax=0.01)

print(f"Final Energy: {slab.get_potential_energy():.4f} eV")
for i, layer_indices in enumerate(layers):
    avg_z = slab.positions[layer_indices, 2].mean()
    print(f"Layer {i+1}: Avg Z = {avg_z:.4f} Å")
