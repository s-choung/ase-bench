import numpy as np
from ase import units
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState

a_values = np.linspace(3.5, 3.7, 7)
volumes, energies = [], []
for a in a_values:
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())
eos = EquationOfState(volumes, energies)
v0, _, _ = eos.fit()
a0 = v0**(1/3)

slab = fcc111('Cu', size=(1, 1, 4), a=a0, vacuum=10.0)
slab.calc = EMT()
constraint = FixAtoms(mask=[tag <= 2 for tag in slab.tags])
slab.set_constraint(constraint)
BFGS(slab, logfile=None).run(fmax=0.01)

print(f"Final energy: {slab.get_potential_energy():.4f}")
for layer in range(1, 5):
    z_avg = np.mean([slab.positions[i][2] for i in range(len(slab)) if slab.tags[i] == layer])
    print(f"Layer {layer} avg z: {z_avg:.4f}")
