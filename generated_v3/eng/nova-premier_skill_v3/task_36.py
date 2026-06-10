import numpy as np
from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

Ag = bulk('Ag', 'fcc', a=4.1); cell = Ag.get_cell()
vols, es = [], []
for s in np.linspace(0.95, 1.05, 7):
    A = Ag.copy(); A.set_cell(cell*s, scale_atoms=True); A.calc = EMT()
    vols.append(A.get_volume())
    es.append(A.get_potential_energy())
eos = EquationOfState(vols, es, eos='birchmurnaghan')
a_eq = (4 * eos.v0 / np.cbrt(2))**(1/3) # fcc structure: V=a³/√2
print(f"a0 = {a_eq:.4f} Å, B0 = {eos.bulk_modulus/units.GPa:.2f} GPa")
