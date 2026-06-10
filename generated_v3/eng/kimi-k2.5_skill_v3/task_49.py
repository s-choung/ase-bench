from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
cell = atoms.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = v0 ** (1/3)

slab = fcc111('Cu', size=(1, 1, 4), vacuum=10.0, a=a_eq)
slab.calc = EMT()
slab.set_constraint(FixAtoms(mask=[a.tag <= 2 for a in slab]))

BFGS(slab).run(fmax=0.05)

print(f"Final energy: {slab.get_potential_energy():.4f} eV")
for tag in sorted({a.tag for a in slab}):
    z_avg = np.mean([a.position[2] for a in slab if a.tag == tag])
    print(f"Layer {tag}: z = {z_avg:.3f} Å")
