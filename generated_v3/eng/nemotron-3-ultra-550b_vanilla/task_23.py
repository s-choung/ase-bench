from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

# Create Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
slab.set_constraint()  # Remove any constraints

# OH molecule
oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.97)])

# Adsorption sites on Pt(111) 2x2 surface
sites = {
    'ontop': (0, 0),
    'bridge': (0.5, 0),
    'fcc': (2/3, 1/3)
}

energies = {}

for name, (x, y) in sites.items():
    # Copy slab and add adsorbate
    system = slab.copy()
    add_adsorbate(system, oh, height=2.0, position=(x, y))
    
    # Calculate energy
    system.calc = EMT()
    energies[name] = system.get_potential_energy()
    print(f"{name}: {energies[name]:.4f} eV")

# Find lowest energy site
lowest = min(energies, key=energies.get)
print(f"\nLowest energy site: {lowest} ({energies[lowest]:.4f} eV)")
