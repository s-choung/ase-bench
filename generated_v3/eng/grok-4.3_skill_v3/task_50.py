import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
a_guess = [3.6, 4.1, 4.1]
print('Metal   a (Å)   B (GPa)')
for m, a0 in zip(metals, a_guess):
    atoms = bulk(m, 'fcc', a=a0)
    cell = atoms.get_cell()
    V, E = [], []
    for x in np.linspace(0.95, 1.05, 7):
        at = atoms.copy()
        at.set_cell(cell * x, scale_atoms=True)
        at.calc = EMT()
        V.append(at.get_volume())
        E.append(at.get_potential_energy())
    eos = EquationOfState(V, E)
    v0, _, B = eos.fit()
    a_eq = v0 ** (1/3)
    print(f'{m:4s}  {a_eq:6.3f}  {B*160.2:6.1f}')
