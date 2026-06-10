import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS

volumes, energies = [], []
for a in np.linspace(3.45, 3.75, 9):
    cu = bulk("Cu", "fcc", a=a, cubic=True)
    cu.calc = EMT()
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())

v0, e0, B = EquationOfState(volumes, energies).fit()
a0 = v0 ** (1 / 3)

slab = fcc111("Cu", size=(1, 1, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

z0 = slab.positions[:, 2]
order = np.argsort(z0)
layers = []
for i in order:
    if not layers or abs(z0[i] - np.mean(z0[layers[-1]])) > 0.2:
        layers.append([i])
    else:
        layers[-1].append(i)

fixed = [i for layer in layers[:2] for i in layer]
slab.set_constraint(FixAtoms(indices=fixed))

BFGS(slab, logfile=None).run(fmax=0.01)

print(f"a0 = {a0:.6f} Å")
print(f"Final energy = {slab.get_potential_energy():.6f} eV")
for n, layer in enumerate(layers, 1):
    print(f"Layer {n} mean z = {slab.positions[layer, 2].mean():.6f} Å")
