from ase import Atoms
from ase.build import fcc111, add_adsorbate, add_vacuum
from ase.calculators.emt import EMT
from ase.data import atomic_numbers

# Create a Pt(111) 4-layer slab
slab = fcc111('Pt', size=(3, 3, 4), vacuum=10.0)

# Add CO molecule on top
co = Atoms(
    symbols=['C', 'O'],
    positions=[[0, 0, 0], [0, 0, 1.1]],
    numbers=[atomic_numbers['C'], atomic_numbers['O']]
)
add_adsorbate(slab, co, height=1.8, position='ontop')

# Optional: relax the slab with EMT calculator (not required for counting atoms)
# slab.calc = EMT()
# relax = BFGS(slab)
# relax.run(fmax=0.05)

# Print the number of atoms in the final structure
print(len(slab))
