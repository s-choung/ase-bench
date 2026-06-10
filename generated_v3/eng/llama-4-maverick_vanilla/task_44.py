from ase import Atoms
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT

slab = Atoms('Cu4Cu4Cu4Cu4', 
             positions=[(0, 0, 0), (2.565, 1.481, 0), (0, 2.962, 0), (2.565, 4.443, 0),
                        (1.2825, 0.7405, 2.087), (3.8475, 2.2215, 2.087), (1.2825, 3.7025, 2.087), (3.8475, 5.1835, 2.087),
                        (0, 0, 4.174), (2.565, 1.481, 4.174), (0, 2.962, 4.174), (2.565, 4.443, 4.174),
                        (1.2825, 0.7405, 6.261), (3.8475, 2.2215, 6.261), (1.2825, 3.7025, 6.261), (3.8475, 5.1835, 6.261)],
             cell=[(5.13, 0, 0), (2.565, 4.443, 0), (0, 0, 8.348)],
             pbc=True)

slab.set_tags([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4])
mask = [atom.tag > 2 for atom in slab]
fixlayers = FixAtoms(mask=mask)
slab.set_constraint(fixlayers)

initial_positions = slab.positions.copy()

slab.calc = EMT()
dyn = BFGS(slab, trajectory='slab.traj')
dyn.run(fmax=0.05)

print("Initial positions of fixed atoms:")
print(slab.positions[mask])
print("Final positions of fixed atoms:")
print(initial_positions[mask])
if (slab.positions[mask] == initial_positions[mask]).all():
    print("Fixed atoms did not move.")
