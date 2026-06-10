import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
cell0 = atoms.get_cell()

volumes, energies = [], []
for x in np.linspace(0.94, 1.06, 9):
    a = atoms.copy()
    a.set_cell(cell0 * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

n_atoms = len(atoms)
v_per_atom = v0 / n_atoms
a_eq = (v0 * 4 / n_atoms) ** (1/3)

print(f"Equilibrium volume (cell): {v0:.4f} Å^3")
print(f"Equilibrium volume (per atom): {v_per_atom:.4f} Å^3")
print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Equilibrium energy: {e0:.4f} eV")
print(f"Bulk modulus: {B / units.kJ * 1e24:.2f} GPa")
