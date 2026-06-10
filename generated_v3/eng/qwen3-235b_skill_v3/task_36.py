from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Ag', 'fcc')
atoms.calc = EMT()

cell0 = atoms.get_cell()
volumes = []
energies = []

for x in np.linspace(0.95, 1.05, 7):
    atoms_scaled = atoms.copy()
    atoms_scaled.set_cell(cell0 * x, scale_atoms=True)
    volumes.append(atoms_scaled.get_volume())
    energies.append(atoms_scaled.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (v0 * 4) ** (1/3)  # fcc conventional cell volume → lattice constant
B_GPa = B / units.GPa

print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
