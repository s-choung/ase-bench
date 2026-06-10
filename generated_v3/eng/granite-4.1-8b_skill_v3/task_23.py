from ase import Atoms
from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Define the OH adsorbate
oh = molecule('OH')

# Create a Pt(111) 3-layer slab with sufficient vacuum
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

# Adsorb OH on the ontop site
add_onsite(  # Assuming the function name is add_onsite for ontop adsorption
    slab, oh, height=1.8, position='onsite'  # Adjust height and position as needed
)

# Adsorb OH on the bridge site
add_onsite(slab, oh, height=1.5, position='bridge')

# Adsorb OH on the fcc hollow site
add_onsite(slab, oh, height=1.7, position='fcc-hollow')

# Function to relax the slab and calculate single-point energy
def compute_energy(atoms):
    mask = [atom.tag >= 3 for atom in atoms]  # Fix the bulk Pt atoms
    atoms.set_constraint(FixAtoms(mask=mask))
    atoms.calc = EMT()
    opt = BFGS(atoms, trajectory=None)
    opt.run(fmax=0.05)
    energy = atoms.get_potential_energy()
    return energy

# Compute energies for each adsorbed configuration
oh_onsite_energy = compute_energy(slab.copy())
oh_bridge_energy = compute_energy(slab.copy())
oh_fcc_hollow_energy = compute_energy(slab.copy())

# Compare and print the results
energies = {
    'onsite': oh_onsite_energy,
    'bridge': oh_bridge_energy,
    'fcc_hollow': oh_fcc_hollow_energy
}
lowest_energy_site = min(energies, key=energies.get)
print(f"The lowest energy site is: {lowest_energy_site} with energy {energies[lowest_energy_site]:.3f} eV")
