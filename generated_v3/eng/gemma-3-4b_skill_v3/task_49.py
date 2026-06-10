import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111, add_adsorbate, fix_positions
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
from ase.spacegroup import crystal
from ase.geometry import get_distances
from ase.visualize import view

# 1. Bulk Cu optimization
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True, orthorhombic=True)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.05, steps=1000)

# 2. Calculate EOS parameters
cell = atoms.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='virial')
v0, e0, B = eos.fit()

print(f"V0: {v0}, E0: {e0}, B: {B}")

# 3. Create (111) 4-layer slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

# 4. Fix bottom 2 layers to match bulk
fix_positions(slab, [i for i in range(3, 5)])  # Fix layers 3 and 4
#Alternative: fix bottom 2 layer atoms
# fix_positions(slab,indices=[0,1])


# 5. Relax slab
opt = BFGS(slab)
opt.run(fmax=0.01)

# 6. Print final energy and z-coordinates
print(f"Slab energy: {slab.get_potential_energy()}")
for layer in range(4):
    distances = get_distances(slab, layer=layer)
    z_coords = slab.cell[2, :]
    print(f"Layer {layer+1} z-coords: {z_coords}")
