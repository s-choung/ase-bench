from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

bottom_layer_indices = [atom.index for atom in slab if atom.tag == 1]
co_indices = [atom.index for atom in slab if atom.symbol in ['C', 'O']]

slab.set_constraint([FixAtoms(indices=bottom_layer_indices), 
                     FixBondLength(co_indices[0], co_indices[1])])

slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

energy = slab.get_potential_energy()
co_distance = slab.get_distance(co_indices[0], co_indices[1])

print(f"Final energy: {energy:.2f} eV")
print(f"C-O distance: {co_distance:.2f} Å")
