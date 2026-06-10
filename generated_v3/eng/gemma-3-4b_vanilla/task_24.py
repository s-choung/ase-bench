from ase.md.lbfgs import LBFGS
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.io import write

cluster = fcc111('Au', size=(4, 4, 4))
calc = EMT(kpts=(4, 4, 4), sigma=0.1, diameter=3.8)
cluster.set_calculator(calc)

optimizer = LBFGS(fmax=0.01)
cluster.run(optimizer)

print(f"Optimization steps: {optimizer.n_steps}")
print(f"Final energy: {cluster.get_potential_energy()}")
write('Au_EMT.xyz', cluster)
