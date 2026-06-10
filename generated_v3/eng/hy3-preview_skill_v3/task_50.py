import numpy as np
from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = {}

for metal in metals:
    # Create FCC bulk structure
    atoms = bulk(metal, 'fcc', cubic=True)
    atoms.calc = EMT()
    
    # Get initial lattice constant
    a0 = atoms.get_cell()[0, 0]
    
    # Vary lattice constant and calculate energies
    volumes = []
    energies = []
    scales = np.linspace(0.95, 1.05, 11)
    
    for scale in scales:
        a = atoms.copy()
        a.set_cell(atoms.get_cell() * scale, scale_atoms=True)
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    
    # Fit Equation of State
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    
    # Calculate equilibrium lattice constant from volume
    # For FCC conventional cell: V = a^3
    a_eq = v0 ** (1/3)
    
    # Convert bulk modulus from eV/Å³ to GPa
    B_GPa = B * 160.21766208  # eV/Å³ to GPa conversion
    
    results[metal] = {'a_eq (Å)': a_eq, 'B (GPa)': B_GPa}

# Print comparison table
print("Metal | Equilibrium lattice constant (Å) | Bulk modulus (GPa)")
print("-" * 55)
for metal in metals:
    a = results[metal]['a_eq (Å)']
    B = results[metal]['B (GPa)']
    print(f"{metal:5} | {a:.3f} | {B:.1f}")
