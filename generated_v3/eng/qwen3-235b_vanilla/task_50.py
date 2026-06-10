from ase.eos import EquationOfState
from ase.build import bulk
from ase.calculators.emt import EMT
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    # Create FCC bulk structure
    atoms = bulk(metal, 'fcc')
    atoms.calc = EMT()
    
    # Volume scaling factors
    cell = atoms.get_cell()
    volumes = []
    energies = []
    for a in np.linspace(0.95, 1.05, 7):
        atoms.set_cell(cell * a, scale_atoms=True)
        volume = atoms.get_volume()
        energy = atoms.get_potential_energy()
        volumes.append(volume)
        energies.append(energy)
    
    # Fit EOS
    eos = EquationOfState(volumes, energies, eos='murnaghan')
    v0, e0, B, B_prime = eos.fit()
    a0 = (v0 / 4) ** (1/3)  # Convert FCC volume to lattice constant
    
    results.append((metal, a0, B))

# Print comparison table
print(f"{'Metal':<5} {'a₀ (Å)':<10} {'Bulk Modulus (eV/Å³)':<20}")
print("-" * 38)
for metal, a0, B in results:
    print(f"{metal:<5} {a0:<10.3f} {B:<20.3f}")
