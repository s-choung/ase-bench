import numpy as np
from ase import Atoms, bulk, units
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Metals to be tested
metals = ['Cu', 'Ag', 'Au']

# Print header
print(f"{'Metal':^5} | {'a0 (Å)':^8} | {'B (GPa)':^8}")
print("-" * 26)

for metal in metals:
    # Initial bulk structure
    atoms = bulk(metal, 'fcc', a=4.0)

    # EOS fitting
    cell = atoms.get_cell()
    volumes, energies = [], []
    for x in np.linspace(0.95, 1.05, 7):
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        a.calc = EMT()
        BFGS(FrechetCellFilter(a)).run(fmax=0.01)  # Optimize cell and positions
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()

    # Equilibrium lattice constant
    a0 = (4 * v0)**(1/3)  # For FCC, V = a^3 / 4

    # Print results
    print(f"{metal:^5} | {a0:^8.3f} | {B / units.GPa:^8.2f}")
