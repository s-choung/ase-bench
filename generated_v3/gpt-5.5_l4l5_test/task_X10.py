from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixedLine
from ase.optimize import BFGS
import numpy as np

slab = fcc111("Pt", size=(2, 2, 4), vacuum=10.0)
add_adsorbate(slab, "H", height=1.1, position="fcc")

pt_indices = [a.index for a in slab if a.symbol == "Pt"]
z_pt = slab.positions[pt_indices, 2]
layers = np.sort(np.unique(np.round(z_pt, 6)))
bottom_layers = layers[:2]
fix_indices = [i for i in pt_indices if np.any(np.isclose(slab.positions[i, 2], bottom_layers))]

h_index = [a.index for a in slab if a.symbol == "H"][0]

slab.set_constraint([
    FixAtoms(indices=fix_indices),
    FixedLine(h_index, direction=[0, 0, 1])
])

slab.calc = EMT()

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.01)

top_pt_z = max(slab.positions[pt_indices, 2])
h_height = slab.positions[h_index, 2] - top_pt_z
energy = slab.get_potential_energy()

print(f"H height: {h_height:.6f} Å")
print(f"Energy: {energy:.6f} eV")
