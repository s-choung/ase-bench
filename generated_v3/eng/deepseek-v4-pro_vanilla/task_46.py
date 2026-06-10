from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase import Atoms

slab = fcc111('Pt', size=(1, 1, 3), a=3.92, vacuum=10.0)

z_positions = slab.positions[:, 2]
z_min = z_positions.min()
bottom_indices = [i for i, z in enumerate(z_positions) if z < z_min + 0.01]

top_index = z_positions.argmax()
top_pos = slab.positions[top_index]

C_pos = top_pos + (0, 0, 2.0)
O_pos = C_pos + (0, 0, 1.15)
co = Atoms('CO', positions=[C_pos, O_pos])
slab.extend(co)

C_index = len(slab) - 2
O_index = len(slab) - 1

constraints = [FixAtoms(indices=bottom_indices),
               FixBondLength(C_index, O_index)]
slab.set_constraint(constraints)

slab.calc = EMT()

opt = BFGS(slab)
opt.run(fmax=0.05)

final_energy = slab.get_potential_energy()
co_distance = slab.get_distance(C_index, O_index)
print(f"Final energy: {final_energy:.6f} eV")
print(f"C-O distance: {co_distance:.3f} Å")
