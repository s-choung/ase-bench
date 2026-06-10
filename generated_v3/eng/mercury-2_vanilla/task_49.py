import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EOSFit
from ase.constraints import FixAtoms

# ----- bulk EOS -----
a_vals = np.linspace(3.3, 4.0, 7)
vol, e = [], []
calc = EMT()
for a in a_vals:
    cu = bulk('Cu', 'fcc', a=a)
    cu.set_calculator(calc)
    vol.append(cu.get_volume() / len(cu))          # per‑atom volume
    e.append(cu.get_potential_energy() / len(cu)) # per‑atom energy
V0, _ = EOSFit(np.array(vol), np.array(e)).fit()
a0 = (4 * V0) ** (1/3)  # FCC relation a³/4 = V_atom

# ----- slab construction -----
slab = fcc111('Cu', size=(1, 1, 4), a=a0, vacuum=10.0)
slab.set_pbc([True, True, False])
slab.set_calculator(EMT())

# fix bottom two layers
layers = slab.get_layer_numbers()
slab.set_constraint(FixAtoms(mask=layers <= 2))

# ----- relaxation -----
BFGS(slab, logfile=None).run(fmax=0.01)

# ----- results -----
print(f'Final energy per atom: {slab.get_potential_energy()/len(slab):.3f} eV')
for i in sorted(set(layers)):
    z_avg = slab.positions[layers == i, 2].mean()
    print(f'Layer {i} avg z = {z_avg:.3f} Å')
