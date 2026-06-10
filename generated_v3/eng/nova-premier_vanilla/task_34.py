from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.neb import NEB
from ase.interpolate import IDPPInterpolator

# Create initial and final state
initial = Atoms('Cu36', cell=(6, 6, 12), pbc=True)
initial.set_calculator(EMT())
initial.rattle(stdev=0.0)
opt = BFGS(initial)
opt.run(fmax=0.01)

fcc_pos = initial.positions[-1]
hcp_pos = fcc_pos.copy()
hcp_pos[:2] += [1.42, 0.82]

initial[-1].position = fcc_pos + [0, 0, 2.0]
final = initial.copy()
final[-1].position = hcp_pos + [0, 0, 2.0]

# Fix bottom layers
mask = [z < 8 for z in initial.positions[:, 2]]
initial.set_constraint(FixAtoms(mask=mask))
final.set_constraint(FixAtoms(mask=mask))

# NEB setup
images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images, interpolate=IDPPInterpolator())
neb.interpolate()

for image in neb.images:
    image.set_calculator(EMT())

optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

e_barrier = max(neb.get_potential_energy_profile()) - neb.get_potential_energy_profile()[0]
print(f"Energy Barrier: {e_barrier:.3f} eV")
