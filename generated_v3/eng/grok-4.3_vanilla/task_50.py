from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units
import numpy as np

metals = ['Cu', 'Ag', 'Au']
init_a = [3.58, 4.09, 4.08]
print(f"{'Metal':<6}{'a (Å)':>10}{'B (GPa)':>10}")
for m, a0 in zip(metals, init_a):
    atoms = bulk(m, 'fcc', a=a0)
    atoms.calc = EMT()
    cell = atoms.get_cell()
    vols, es = [], []
    for s in np.linspace(0.95, 1.05, 7):
        atoms.set_cell(cell * s, scale_atoms=True)
        vols.append(atoms.get_volume())
        es.append(atoms.get_potential_energy())
    eos = EquationOfState(vols, es)
    v0, _, B = eos.fit()
    a = (4 * v0) ** (1/3)
    B_gpa = B * 160.2177
    print(f"{m:<6}{a:>10.3f}{B_gpa:>10.1f}")
