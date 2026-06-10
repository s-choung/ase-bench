import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

volumes, energies = [], []
for a in np.linspace(3.4, 3.8, 9):
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = v0 ** (1.0 / 3.0)

slab = fcc111('Cu', size=(2, 2, 4), a=a0, vacuum=10.0)
slab.calc = EMT()
slab.set_constraint(FixAtoms(mask=slab.get_tags() <= 2))

BFGS(slab).run(fmax=0.01)

print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Final energy: {slab.get_potential_energy():.4f} eV")

tags = slab.get_tags()
z = slab.positions[:, 2]
for layer in sorted(set(tags)):
    print(f"Layer {layer} avg z: {np.mean(z[tags == layer]):.4f} Å")
