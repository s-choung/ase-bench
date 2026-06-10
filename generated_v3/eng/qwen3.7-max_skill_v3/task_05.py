import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import GPa

atoms = bulk('Cu', 'fcc', a=3.6)
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

a0 = (4 * v0)**(1/3)

print(f"Equilibrium volume (primitive cell): {v0:.4f} Å^3")
print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Bulk modulus: {B:.4f} eV/Å^3 ({B / GPa:.2f} GPa)")
