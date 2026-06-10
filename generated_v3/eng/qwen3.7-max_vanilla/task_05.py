import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import GPa

volumes = []
energies = []

for a in np.linspace(3.4, 3.8, 9):
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (4 * v0)**(1/3)

print(f"Equilibrium Volume: {v0:.4f} Å^3")
print(f"Bulk Modulus: {B * GPa:.2f} GPa")
print(f"Equilibrium Lattice Constant: {a0:.4f} Å")
