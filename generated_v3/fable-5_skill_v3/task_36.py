import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09)
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

a0 = (4 * v0) ** (1 / 3)  # FCC primitive cell: V = a^3/4
B_GPa = B / units.kJ * 1.0e24  # eV/Å³ → GPa

print(f"Equilibrium volume: {v0:.4f} Å³")
print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
print(f"Minimum energy: {e0:.6f} eV")
