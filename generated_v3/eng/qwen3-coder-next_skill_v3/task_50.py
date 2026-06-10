import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import GPa

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    # Create initial FCC bulk structure
    atoms = bulk(metal, 'fcc', a=3.6)
    atoms.calc = EMT()
    
    # Generate volume/energy points
    volumes, energies = [], []
    for x in np.linspace(0.95, 1.05, 7):
        a = atoms.copy()
        cell = a.get_cell()
        a.set_cell(cell * x, scale_atoms=True)
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    
    # Fit EOS
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    
    # Convert to lattice constant (FCC: V = a^3/4 → a = (4V)^(1/3))
    a_eq = (4 * v0) ** (1/3)
    
    results.append((metal, a_eq, B / GPa))

# Print comparison table
print("=" * 50)
print(f"{'Metal':<10} {'a_eq (Å)':<15} {'B (GPa)':<15}")
print("=" * 50)
for metal, a_eq, B_GPa in results:
    print(f"{metal:<10} {a_eq:<15.4f} {B_GPa:<15.2f}")
print("=" * 50)
