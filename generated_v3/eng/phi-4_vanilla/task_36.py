from ase import Atoms
from ase.calculators.emt import EMT
from numpy import linspace
import json
import numpy as np
from scipy.optimize import curve_fit

# Define a Birch-Murnaghan EOS fitting function
def birch_murnaghan(V, E0, B0, B0_prime, V0):
    eta = (V0/V)**(2/3)
    return E0 + (9 * V0 * B0 / 16) * ((eta - 1)**3 * B0_prime + (eta - 1)**2 * (6 - 4 * eta))

# Function to fit the EOS
def fit_eos(volumes, energies):
    B0_guess = max(energies) - (energies[-1] - energies[-2]) / (volumes[-1] - volumes[-2])
    V0_guess = min(volumes)

    E0_guess = energies[0]
    B0_prime_guess = 4

    initial_guess = [E0_guess, B0_guess, B0_prime_guess, V0_guess]
    bounds = (0, [np.inf, np.inf, np.inf, np.inf])

    params, _ = curve_fit(birch_murnaghan, volumes, energies, p0=initial_guess, bounds=bounds)

    E0, B0, B0_prime, V0 = params
    return B0, V0

# Create Ag atoms
lattice_constant = 4.0852
atom = Atoms('Ag', positions=[(0, 0, 0)])
atom.set_cell([lattice_constant]*3, scale=True)
atom.pbc = (True, True, True)

# Set up EMT calculator for bulk Ag
calculator = EMT()
atom.set_calculator(calculator)

# Calculate equilibrium volume and bulk modulus
initial_volume = lattice_constant ** 3
initial_energy = atom.get_potential_energy()

# Lattice constant variation within +/- 5%
variation_percentages = linspace(-0.05, 0.05, 7)
volumes = [(1 + v) * initial_volume for v in variation_percentages]
energies = [calculator.get_potential_energy(Atoms('Ag', positions=[(0, 0, 0)]).set_cell((v ** (1/3)) * np.identity(3), scale=True) for v in volumes]

# Fit materials using Birch-Murnaghan EOS
B0, V0 = fit_eos(volumes, energies)

# Report results as JSON data
results = {
    "equilibrium_lattice_constant": V0 ** (1/3),
    "bulk_modulus": B0,
}

print(json.dumps(results, indent=4))
