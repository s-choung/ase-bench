from ase import Atoms
from ase.build import fcc111_slab, add_adsorbate
from ase.calculators import EMT, LJ
from ase.io import write

# Create Pt(111) 3-layer slab
slab = fcc111_slab(1, size=(3, 3, 3), vacuum=1.0)

# Adsorb OH molecule
slab.add_adsorbate(site='on-top', coverage=1)
slab.add_adsorbate(site='bridge', coverage=1)
slab.add_adsorbate(site='fcc', coverage=1)

# Attach EMT calculator to each structure
calc_ontop = EMT()
calc_bridge = EMT()
calc_fcc = EMT()

slab.calc = calc_ontop
slab.add_adsorbate(site='on-top', coverage=1)

slab.calc = calc_bridge
slab.add_adsorbate(site='bridge', coverage=1)

slab.calc = calc_fcc
slab.add_adsorbate(site='fcc', coverage=1)


# Compute single-point energies
energy_ontop = slab.get_potential_energy()
energy_bridge = slab.get_potential_energy()
energy_fcc = slab.get_potential_energy()

# Print the results
print(f"Energy on-top: {energy_ontop}")
print(f"Energy bridge: {energy_bridge}")
print(f"Energy fcc: {energy_fcc}")

if energy_ontop < energy_bridge and energy_ontop < energy_fcc:
    print("On-top site has the lowest energy.")
elif energy_bridge < energy_ontop and energy_bridge < energy_fcc:
    print("Bridge site has the lowest energy.")
else:
    print("Fcc site has the lowest energy.")
