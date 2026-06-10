from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

def calculate_eos(metal, symbol):
    atoms = bulk(symbol, 'fcc', a=4.0)  # Initial guess for the lattice constant
    atoms.calc = EMT()
    
    volumes, energies = [], []
    for x in np.linspace(0.95, 1.05, 9):
        atoms.set_cell(atoms.get_initial_lattice_vectors() * x, scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a0 = (4 * v0)**(1/3)

    return a0, B / 1.60218e-1  # Convert bulk modulus to GPa

metals = {'Copper': 'Cu', 'Silver': 'Ag', 'Gold': 'Au'}
results = {name: calculate_eos(name, symbol) for name, symbol in metals.items()}

print(f"{'Metal':<10} {'a0 (Å)':<10} {'B (GPa)':<10}")
for metal, (a0, B) in results.items():
    print(f"{metal:<10} {a0:<10.2f} {B:<10.2f}")
