from ase.build import fcc
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import BirchMurnaghan

atoms = fcc('Ag', size=3.0)
calc = EMT()
atoms.calc = calc

volumes = []
energies = []
a0 = atoms.get_cell_size()[0]

for i in range(7):
    a = a0 * (1 + (i - 3) * 0.1)
    atoms.set_cell([a, a, a], 'xyz')
    atoms.get_positions('direct')
    energy = atoms.calc.get_potential_energy()
    volumes.append(atoms.get_volume())
    energies.append(energy)

fit = BirchMurnaghan(volumes, energies, eos_dtype='perry')
V0, B0 = fit.fit()

print(f'Equilibrium volume: {V0:.3f} Bohr^3')
print(f'Equilibrium lattice constant: {V0** (1/3) * 2:.6f} Angstrom')
print(f'Bulk modulus: {B0:.2f} GPa')
