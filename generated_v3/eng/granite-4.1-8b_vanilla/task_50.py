from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = {'Cu': 3.615, 'Ag': 4.089, 'Au': 4.078}  # initial guessed lattice constants in Å

results = []

for symbol, a0 in metals.items():
    # Create FCC bulk structure
    cell = 4 * a0 / np.sqrt(2)  # side length for FCC cell with nearest-neighbor distance a0
    cu = Atoms('FCC', cell=cell, pbc=True)
    cu.set_positions(np.array([
        [0.0, 0.0, 0.0],
        [0.5, 0.5, 0.0],
        [0.5, 0.0, 0.5],
        [0.0, 0.5, 0.5],
    ]))
    cu *= (len(cu) // 4, 4, 4)  # scale to larger cell

    # Set calculator
    cu.set_calculator(EMT())

    # Generate lattice constants for EOS fitting
    lattice_constants = np.linspace(a0 * 0.9, a0 * 1.1, 7)
    energies = []

    for a in lattice_constants:
        cu.cell = 4 * a / np.sqrt(2) * np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]) / np.sqrt(2)  # update cell
        energies.append(cu.get_potential_energy())

    # Fit EOS
    eos = EquationOfState(lattice_constants, energies)
    a_eq, v_eq, b_eq = eos.fit()

    results.append((symbol, a_eq, b_eq))

# Print comparison table
print(f"{'Metal':<3} {'a_eq (Å)':>11} {'B (GPa)':>9}")
print("-" * 32)
for symbol, a_eq, b_eq in results:
    print(f"{symbol:<3} {a_eq:>11.3f} {b_eq/100:>.2f}")
