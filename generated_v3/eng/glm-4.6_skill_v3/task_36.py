import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

a0 = 4.09  # Initial guess for Ag lattice constant
atoms = bulk('Ag', 'fcc', a=a0)
atoms.calc = EMT()

volumes, energies = [], []
for scale in np.linspace(0.95, 1.05, 7):
    a = a0 * scale
    atoms.set_cell([a, a, a], scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = (v0 / 4)**(1/3)  # Convert volume to lattice constant for FCC

print(f"Equilibrium lattice constant: {a_eq:.3f} Å")
print(f"Bulk modulus: {B / units.J * 1e-21:.1f} GPa")  # Convert eV/Å³ to GPa
