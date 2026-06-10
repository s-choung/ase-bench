from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
from ase.optimize import BFGS
import numpy as np

a_values = np.linspace(3.5, 3.8, 10)
energies = []
volumes = []
for a in a_values:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a_eq = v0 ** (1/3)

slab = fcc111('Cu', size=(1, 1, 4), a=a_eq, vacuum=10.0)
z = slab.positions[:, 2]
sorted_idx = np.argsort(z)
n = len(slab) // 4
layers = [sorted_idx[i*n:(i+1)*n] for i in range(4)]
slab.set_constraint(FixAtoms(indices=np.concatenate(layers[:2])))

slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.01)

print(f"Final energy: {slab.get_potential_energy():.4f} eV")
print("Average z-coordinate per layer:")
for i, layer in enumerate(layers):
    print(f"  Layer {i+1}: {np.mean(slab.positions[layer, 2]):.3f} Å")
