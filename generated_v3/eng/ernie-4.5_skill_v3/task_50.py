import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import kJ, mol

# Metals to investigate
metals = ['Cu', 'Ag', 'Au']
results = {}

for metal in metals:
    # Create FCC bulk structure with initial guess for a
    atoms = bulk(metal, 'fcc', a=4.0)
    atoms.calc = EMT()
    
    # Generate different volumes (strained cells)
    volumes = []
    energies = []
    
    for x in np.linspace(0.9, 1.1, 11):
        a = atoms.copy()
        a.set_cell(atoms.cell * x, scale_atoms=True)
        a.calc.reset()  # Reset calculator to clear old results
        e = a.get_potential_energy()
        volumes.append(a.get_volume())
        energies.append(e)
    
    # Fit to Birch-Murnaghan EOS
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (4 * v0)**(1/3)  # FCC lattice constant from primitive cell volume
    
    results[metal] = {
        'a0': a0,
        'B': B * (kJ/mol**-1 * 1e-21 / 1e-30)  # Convert to GPa (1 GPa = 1e9 Pa)
        # Alternative: B * 160.21773  # Exact conversion factor from eV/Å³ to GPa
    }
    # Simplified conversion: 1 eV/Å³ ≈ 160.21773 GPa
    # Using above conversion for clarity
    results[metal]['B'] = B * 160.21773  

# Print comparison table
print(f"{'Metal':<5} {'a0 (Å)':<12} {'B (GPa)':<12}")
print("-" * 30)
for metal in metals:
    print(f"{metal:<5} {results[metal]['a0']:.4f}   {results[metal]['B']:.2f}")
