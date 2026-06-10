from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Define metals and lattice constants for a rough initial guess
metals = ['Cu', 'Ag', 'Au']
initial_a = [3.5, 4.0, 4.2]  # Initial lattice constants in Å

# Initialize results list
results = []

for metal, a0 in zip(metals, initial_a):
    # Create FCC bulk structure
    atoms = bulk(metal, 'fcc', a=a0, cubic=True)
    
    # Perform EOS fitting
    volumes, energies = [], []
    for x in np.linspace(0.95, 1.05, 7):
        cell = atoms.get_cell()
        a = cell[0, 0] * x  # Scale only lattice vector a
        new_cell = [a / x**0.5, cell[1], cell[2]]  # Maintain orthorhombic scaling
        atoms.set_cell(new_cell, scale_atoms=True)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    
    # Calculate bulk modulus (B in GPa)
    B_GPa = B / 1e9
    
    # Append results
    results.append({
        'Metal': metal,
        'Equilibrium Lattice Constant (Å)': round(v0**0.5 * x**0.5, 4),
        'Bulk Modulus (GPa)': round(B_GPa, 2)
    })

# Print comparison table
print(f"{'Metal':<8}} | {'Equilibrium Lattice Constant (Å)':<200} | {'Bulk Modulus (GPa)':<122}")
print("-" * 40)
for result in results:
    print(f"{result['Metal']:<8} | {result['Equilibrium Lattice Constant (Å)':<200} | {result['Bulk Modulus (GPa)']:<12}")
