from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Conversion factor: eV/Å³ to GPa
EVPA3_TO_GPA = 160.21766208
metals = ['Cu', 'Ag', 'Au']
results = []

# Run EOS calculation for each metal
for sym in metals:
    # Base FCC structure
    atoms = bulk(sym, 'fcc')
    volumes, energies = [], []
    
    # Generate scaled unit cells
    for scale in np.linspace(0.92, 1.08, 11):
        scaled_atoms = atoms.copy()
        scaled_atoms.set_cell(atoms.cell * scale, scale_atoms=True)
        scaled_atoms.calc = EMT()
        energies.append(scaled_atoms.get_potential_energy())
        volumes.append(scaled_atoms.get_volume())
    
    # Fit Birch-Murnaghan EOS
    eos = EquationOfState(volumes, energies)
    v0, _, B0 = eos.fit()
    a0 = v0 ** (1/3)  # Extract lattice constant from equilibrium FCC cell volume
    results.append((sym, f"{a0:.4f}", f"{B0 * EVPA3_TO_GPA:.1f}"))

# Print formatted comparison table
print("\nEOS Fitting Results (EMT Calculator) for FCC Noble Metals")
print("+" + "-"*7 + "+" + "-"*21 + "+" + "-"*19 + "+")
print(f"| {'Metal':<5} | {'Equilibrium a0 (Å)':<19} | {'Bulk Modulus (GPa)':<17} |")
print("+" + "-"*7 + "+" + "-"*21 + "+" + "-"*19 + "+")
for res in results:
    print(f"| {res[0]:<5} | {res[1]:<19} | {res[2]:<17} |")
print("+" + "-"*7 + "+" + "-"*21 + "+" + "-"*19 + "+\n")
