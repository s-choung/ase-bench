import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    atoms = cu.copy()
    atoms.set_cell(cu.cell * x, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (4 * v0) ** (1/3)
print(f"Optimal lattice constant: {a0:.4f} Å")

slab = fcc111('Cu', size=(2, 2, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

z_coords = slab.positions[:, 2]
unique_z = np.sort(np.unique(np.round(z_coords, 3)))
mask = [z < unique_z[2] - 0.01 for z in z_coords]
slab.set_constraint(FixAtoms(mask=mask))

opt = BFGS(slab)
opt.run(fmax=0.05)

print(f"Final energy: {slab.get_potential_energy():.4f} eV")

tags = slab.get_tags()
for layer in sorted(set(tags)):
    z_mean = slab.positions[tags == layer, 2].mean()
    print(f"Layer {layer}: z_mean = {z_mean:.4f} Å")
