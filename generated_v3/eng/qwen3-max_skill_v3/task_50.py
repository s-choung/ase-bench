import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    # Create initial FCC bulk structure
    atoms = bulk(metal, 'fcc', a=4.0)
    atoms.calc = EMT()
    
    # Generate EOS data
    volumes = []
    energies = []
    cell0 = atoms.get_cell()
    for x in np.linspace(0.95, 1.05, 7):
        a = atoms.copy()
        a.set_cell(cell0 * x, scale_atoms=True)
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    
    # Fit EOS
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (4 * v0)**(1/3)  # FCC: V = a^3/4 → a = (4V)^(1/3)
    B_GPa = B / units.GPa
    results.append((metal, a0, B_GPa))

# Print comparison table
print(f"{'Metal':<6} {'a₀ (Å)':<10} {'B (GPa)':<10}")
print("-" * 25)
for metal, a0, B in results:
    print(f"{metal:<6} {a0:<10.4f} {B:<10.1f}")
