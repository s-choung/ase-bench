from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

d = 5.0
fixed = [0, 2]

# Initial: moving atom near left fixed atom
initial = Atoms('Al3',
                positions=[[0, 0, 0], [2.0, 0, 0], [d, 0, 0]],
                cell=[10, 10, 10], pbc=False)
initial.calc = EMT()

# Final: moving atom near right fixed atom
final = Atoms('Al3',
              positions=[[0, 0, 0], [3.0, 0, 0], [d, 0, 0]],
              cell=[10, 10, 10], pbc=False)
final.calc = EMT()

# Build band: initial + 3 intermediates + final
images = [initial] + [initial.copy() for _ in range(3)] + [final]
for img in images:
    img.set_constraint(FixAtoms(indices=fixed))

neb = NEB(images)
neb.interpolate(method='linear')

for img in images[1:-1]:
    img.calc = EMT()

BFGS(neb, trajectory='neb.traj').run(fmax=0.05, steps=200)

print("NEB results (Al atom hopping between two fixed Al atoms):")
for i, img in enumerate(images):
    e = img.get_potential_energy()
    x = img.positions[1][0]
    label = "initial" if i == 0 else ("final" if i == len(images) - 1 else f"image {i}")
    print(f"  {label:>8s}: E = {e:.6f} eV, moving atom x = {x:.3f} Å")
