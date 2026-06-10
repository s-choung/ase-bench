from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk, fcc111
from ase.eos import EquationOfState
from ase.optimize import BFGS
import numpy as np

# EOS fitting
atoms = bulk("Cu", "fcc")
calc = EMT()
vol = []; e_pot = []
for a in np.linspace(3.4, 3.8, 7):
    tmp = atoms.copy()
    tmp.set_cell(tmp.get_cell()*a/3.6, scale_atoms=True)
    tmp.calc = calc
    vol.append(tmp.get_volume())
    e_pot.append(tmp.get_potential_energy())
eos = EquationOfState(vol, e_pot)
v0, e0, _ = eos.fit()
a_eq = (v0/atoms.get_volume())**(1/3)*3.6  # Original cell was 3.6Å

# Slab creation
slab = fcc111("Cu", (2,2,4), vacuum=10.0, a=a_eq)
slab.calc = EMT()
fixed = [n for n in range(8)]  # Bottom 2 layers

# Relaxation
opt = BFGS(slab, trajectory="relax.traj")
opt.run(fmax=0.02)

# Analysis
layers = [(slab.positions[:,2] >= h-0.5) & (slab.positions[:,2] < h+1.5)
           for h in np.unique(slab.positions[:,2]-0.5)]
final_energy = slab.get_potential_energy()
print(f"Energy: {final_energy:.3f} eV")
for i, layer in enumerate(layers):
    print(f"Layer {i+1} avg z: {slab.positions[layer,2].mean():.3f} Å")
