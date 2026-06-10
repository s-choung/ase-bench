import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import kJ

cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()
a0 = cu.cell.cellpar()[0]

volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 9):
    atoms = cu.copy()
    atoms.set_cell(cu.cell * x, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = (4 * v0) ** (1/3)
print(f"Equilibrium volume per atom: {v0:.4f} Å^3")
print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B / kJ * 1e24:.2f} GPa")
