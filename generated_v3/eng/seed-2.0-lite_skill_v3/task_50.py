import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Process each FCC metal
metals = ['Cu', 'Ag', 'Au']
results = {}
for metal in metals:
    # Create base cubic FCC bulk structure
    atoms = bulk(metal, 'fcc', a=3.8, cubic=True)
    volumes, energies = [], []
    # Scale cell around equilibrium to generate EOS data points
    for scale in np.linspace(0.95, 1.05, 7):
        scaled_atoms = atoms.copy()
        scaled_atoms.set_cell(atoms.cell * scale, scale_atoms=True)
        scaled_atoms.calc = EMT()
        volumes.append(scaled_atoms.get_volume())
        energies.append(scaled_atoms.get_potential_energy())
    # Fit Birch-Murnaghan equation of state
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, _, B = eos.fit()
    # Calculate equilibrium lattice constant (cubic cell: v0 = a0³)
    a0 = v0 ** (1/3)
    # Convert bulk modulus from eV/Å³ to GPa
    B_gpa = B * (units.eV / units.Å**3) / units.GPa
    results[metal] = (a0, B_gpa)

# Print formatted comparison table
print(f"{'Metal':<6} {'a₀ (Å)':<10} {'B (GPa)':<10}")
print("-" * 26)
for metal in metals:
    a0, b = results[metal]
    print(f"{metal:<6} {a0:.3f}{'':<4} {b:.1f}{'':<4}")
