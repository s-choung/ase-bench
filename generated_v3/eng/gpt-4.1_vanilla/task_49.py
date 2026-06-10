from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# 1. EOS to find equilibrium lattice constant
a0 = 3.6
atoms_bulk = bulk('Cu', 'fcc', a=a0)
atoms_bulk.calc = EMT()
volumes, energies = [], []
for scale in np.linspace(0.96, 1.04, 7):
    atoms = atoms_bulk.copy()
    atoms.set_cell(atoms.get_cell()*scale, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
alat = (v0/4)**(1/3)  # 4 atoms per cell

# 2. Build (111) 4-layer slab
slab = fcc111('Cu', size=(1,1,4), a=alat, vacuum=8.0)
slab.calc = EMT()

# 3. Fix bottom 2 layers
zs = slab.positions[:,2]
zmin = min(zs)
zmax = max(zs)
layer_z = np.unique(np.round(zs,3))
bottom_layers = layer_z[:2]
fix_mask = [np.isclose(z, bottom_layers[0], atol=0.01) or np.isclose(z, bottom_layers[1], atol=0.01) for z in zs]
slab.set_constraint(FixAtoms(mask=fix_mask))

# 4. Relax
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.02)

# 5. Output energy and average z per layer
print(f'Relaxed energy: {slab.get_potential_energy():.6f} eV')
z_coords = slab.positions[:,2]
for i, zval in enumerate(np.sort(layer_z)):
    layer_atoms = np.where(np.isclose(z_coords, zval, atol=0.01))[0]
    avgz = np.mean(z_coords[layer_atoms])
    print(f'Layer {i+1} avg z: {avgz:.3f} Å')
