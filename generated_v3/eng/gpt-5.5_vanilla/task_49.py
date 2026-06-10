import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS

a_values = np.linspace(3.45, 3.75, 9)
volumes, energies = [], []

for a in a_values:
    atoms = bulk("Cu", "fcc", a=a)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (4.0 * v0) ** (1.0 / 3.0)

slab = fcc111("Cu", size=(2, 2, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

z0 = slab.positions[:, 2]
levels = np.array(sorted(set(np.round(z0, 6))))
layer_id = np.array([np.argmin(abs(levels - z)) for z in z0])

slab.set_constraint(FixAtoms(mask=layer_id < 2))

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.02)

print(f"Equilibrium lattice constant: {a0:.6f} Å")
print(f"Final energy: {slab.get_potential_energy():.6f} eV")

for i in range(len(levels)):
    avg_z = slab.positions[layer_id == i, 2].mean()
    print(f"Layer {i + 1}: average z = {avg_z:.6f} Å")
