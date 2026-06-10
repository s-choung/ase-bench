import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

a0 = 4.0
atoms_ref = bulk('Ag', 'fcc', a=a0)
cell_ref = atoms_ref.get_cell()

volumes, energies = [], []

for x in np.linspace(0.95, 1.05, 7):
    atoms = atoms_ref.copy()
    atoms.set_cell(cell_ref * x, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# v0 is volume of the unit cell. For FCC, v0 = a0^3 / 4 -> a0 = (4 * v0)**(1/3)
a_eq = (4 * v0) ** (1/3)
B_GPa = B / units.GPa

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
