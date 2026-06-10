from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0 = 4.086
strain_range = np.linspace(-0.05, 0.05, 7)

energies = []
volumes = []

for strain in strain_range:
    cell = fcc111('Ag', size=(2, 2, 2), latticeconstant=a0 * (1 + strain))
    calc = EMT()
    cell.calc = calc
    energy = cell.get_potential_energy()
    energies.append(energy)
    volumes.append(cell.get_volume())

eos = EquationOfState(volumes, energies)
a_eq, b_eq, B_eq = eos.fit(plot=False)
a_eq_angstroms = a_eq
a_eq_bohr = a_eq_angstroms * 1.88973
B_eq_GPa = B_eq

print(f"Equilibrium lattice constant: {a_eq_angstroms:.4f} Angstroms")
print(f"Bulk modulus: {B_eq_GPa:.2f} GPa")
