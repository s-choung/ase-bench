import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

a0 = 4.09
atoms = bulk('Ag', 'fcc', a=a0)
cell = atoms.get_cell()

V, E = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    V.append(a.get_volume())
    E.append(a.get_potential_energy())

v0, e0, B = EquationOfState(V, E, eos='birchmurnaghan').fit()
a_eq = v0 ** (1/3)
B_GPa = B * units.eV / units.Ang**3 / units.GPa

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
