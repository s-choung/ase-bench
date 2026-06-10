import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', a=3.5, cubic=True)
volumes, energies = [], []
for x in np.linspace(0.94, 1.06, 7):
    a = atoms.copy()
    a.set_cell(atoms.cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (4.0 * v0) ** (1.0 / 3.0)

slab = fcc111('Cu', size=(1, 1, 4), a=a0, vacuum=10.0, orthogonal=True)
slab.calc = EMT()
slab.set_constraint(FixAtoms(mask=[atom.tag <= 2 for atom in slab]))

BFGS(slab).run(fmax=0.05)

print(f"Final energy: {slab.get_potential_energy():.6f} eV")
for tag in sorted(set(slab.get_tags())):
    zavg = np.mean([atom.position[2] for atom in slab if atom.tag == tag])
    print(f"Layer {tag}: avg z = {zavg:.6f} Å")
