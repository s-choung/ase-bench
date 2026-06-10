import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import kJ

a0 = 4.09
atoms = bulk('Ag', 'fcc', a=a0)
scales = np.linspace(0.95, 1.05, 7)
volumes, energies = [], []

for s in scales:
    a = atoms.copy()
    a.set_cell(atoms.cell * s, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = (4 * v0) ** (1/3)
B_GPa = B / kJ * 1.0e24

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
