from ase.build import fcc111, molecule
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import MDMin

# Create Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Define OH molecule
oh = molecule('OH')

# Function to adsorb OH on slab and calculate energy
def adsorb_and_calculate(slab, oh, position):
    slab_with_oh = slab.copy()
    slab_with_oh.extend(oh)
    slab_with_oh.center(axis=2, vacuum=10.0)
    if position == 'ontop':
        slab_with_oh[-2].position = slab_with_oh[0].position + [0, 0, 1.5]
    elif position == 'bridge':
        slab_with_oh[-2].position = (slab_with_oh[0].position + slab_with_oh[1].position) / 2 + [0, 0, 1.5]
    elif position == 'fcc':
        slab_with_oh[-2].position = (slab_with_oh[0].position + slab_with_oh[1].position + slab_with_oh[2].position) / 3 + [0, 0, 1.5]
    slab_with_oh.set_constraint(FixAtoms(mask=[a.symbol != 'O' and a.symbol != 'H' for a in slab_with_oh]))
    slab_with_oh.set_calculator(EMT())
    MDMin(slab_with_oh, trajectory=None).run(fmax=0.05)
    return slab_with_oh.get_potential_energy()

# Calculate energies for each site
ontop_energy = adsorb_and_calculate(slab, oh, 'ontop')
bridge_energy = adsorb_and_calculate(slab, oh, 'bridge')
fcc_energy = adsorb_and_calculate(slab, oh, 'fcc')

# Determine and print the lowest energy site
min_energy = min(ontop_energy, bridge_energy, fcc_energy)
if min_energy == ontop_energy:
    print("On-top site has the lowest energy.")
elif min_energy == bridge_energy:
    print("Bridge site has the lowest energy.")
else:
    print("Fcc hollow site has the lowest energy.")
