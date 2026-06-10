import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

volumes, energies = [], []
for a in np.linspace(3.4, 3.8, 20):
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = eos.get_lattice_constant('fcc')

slab = fcc111('Cu', size=(1, 1, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

z = slab.get_positions()[:, 2]
z_unique = sorted(list(set(np.round(z, 2))))
mask = [atom.position[2] <= z_unique[1] for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.01)

print(f"Final Energy: {slab.get_potential_energy():.4f} eV")
z_final = np.sort(slab.get_positions()[:, 2])
atoms_per_layer = len(z_final) // 4
for i in range(4):
    start, end = i * atoms_per_layer, (i + 1) * atoms_per_layer
    print(f"Layer {i+1} Avg Z: {z_final[start:end].mean():.4f} A")
