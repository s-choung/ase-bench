import numpy as np
from ase import units
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.filters import FrechetCellFilter
from ase.eos import EquationOfState

# 1. Equilibrium lattice constant via EOS
atoms_bulk = bulk('Cu', 'fcc', a=3.6)
atoms_bulk.calc = EMT()
volumes, energies = [], []

for x in np.linspace(0.9, 1.1, 7):
    a = atoms_bulk.copy()
    a.set_cell(atoms_bulk.get_cell() * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = (v0 / (1.0/4.0))**(1/3) # FCC primitive cell volume v0 = a^3 / 4 (standard bulk('Cu', 'fcc') is primitive)
# Since bulk('Cu', 'fcc') returns a primitive cell, the volume is a^3/4. 
# However, for clarity, we can calculate it from the scaled unit cell:
a_eq = (v0 * 4)**(1/3) if atoms_bulk.get_cell().volume == (3.6**3 / 4) else v0**(1/3)
# Re-calculating a_eq simply by using the fitted v0 relative to the initial a=3.6:
a_eq = 3.6 * (v0 / atoms_bulk.get_volume())**(1/3)

# 2. Create (111) slab with equilibrium lattice constant
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=a_eq)
slab.calc = EMT()

# 3. Fix bottom 2 layers
# Each layer in fcc111(size=(2,2,4)) has 2*2 = 4 atoms.
mask = [False] * len(slab)
for i in range(2 * 4): # first two layers
    mask[i] = True
slab.set_constraint(FixAtoms(mask=mask))

# 4. Surface Relaxation
opt = BFGS(slab)
opt.run(fmax=0.05)

# 5. Results
print(f"Final Energy: {slab.get_potential_energy():.4f} eV")
z_coords = slab.get_positions()[:, 2]
for layer in range(4):
    layer_z = z_coords[layer*4 : (layer+1)*4]
    print(f"Layer {layer} avg z: {np.mean(layer_z):.4f} Å")
