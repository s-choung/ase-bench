import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS

a0 = 3.60
scales = np.linspace(0.94, 1.06, 9)
volumes, energies = [], []

for s in scales:
    atoms = bulk("Cu", "fcc", a=a0 * s)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos="birchmurnaghan")
v0, e0, B = eos.fit()
a_eq = (4.0 * v0) ** (1.0 / 3.0)

slab = fcc111("Cu", size=(2, 2, 4), a=a_eq, vacuum=12.0)
slab.calc = EMT()

tags = slab.get_tags()
slab.set_constraint(FixAtoms(mask=tags >= 3))

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.03, steps=200)

print(f"Equilibrium FCC lattice constant: {a_eq:.6f} Å")
print(f"Final slab energy: {slab.get_potential_energy():.6f} eV")

tags = slab.get_tags()
for i, tag in enumerate(sorted(set(tags), key=lambda t: slab.positions[tags == t, 2].mean()), 1):
    zavg = slab.positions[tags == tag, 2].mean()
    print(f"Layer {i} average z: {zavg:.6f} Å")
