import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

atoms_base = bulk('Ag', 'fcc', cubic=True)
cell_base = atoms_base.get_cell()

volumes, energies = [], []
for scale in np.linspace(0.95, 1.05, 7):
    atoms = atoms_base.copy()
    atoms.set_cell(cell_base * scale, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a0 = v0 ** (1.0 / 3.0)
B_GPa = B / units.GPa

print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
