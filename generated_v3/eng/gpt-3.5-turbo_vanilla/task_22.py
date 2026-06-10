from ase.build import fcc111, molecule
from ase.adsorption import AdsorbateSiteFinder
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton

# Create Al(111) slab with 3 layers
slab = fcc111('Al', size=(3, 3, 3), vacuum=10.0)

# Adsorbate: N2 molecule
N2 = molecule('N2')
N2.translate([0, 0, 2.0])  # Place N2 at a height of 2.0 angstroms above the slab

# Combine slab and adsorbate
slab_N2 = slab + N2

# Find adsorption site
asf = AdsorbateSiteFinder(slab, symm_reduce=0.0)
adsorption_site = asf.get_ideal_adsorption_site(N2)

# Set the EMT calculator
slab_N2.calc = EMT()

# Optimize the structure
dyn = QuasiNewton(slab_N2)
dyn.run(fmax=0.05)  # Stop optimization when the forces are less than 0.05 eV/angstrom

# Print the number of atoms and atom types
print('Number of atoms:', len(slab_N2))
print('Atom types:', set(slab_N2.get_chemical_symbols()))
