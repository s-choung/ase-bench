from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators import EMT, LJ
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

calc = EMT(pseudized=True)
slab = fcc111('Pt', size=(3, 3, 3), vacuum=1.0)
calc.set_functional('LDA')
slab.set_calculator(calc)

add_adsorbate(slab, 'CO', height=2.0, position='ontop')

fix_bottom = FixAtoms(indices=range(slab.get_number_of_atoms() - 2))
fix_co = FixBondLength(charge=1, index1=slab.indices.co, index2=slab.indices.co)
slab.add_constraints(fix_bottom, fix_co)

dyn = BFGS(slab, trajectory='co_adsorption.traj')
dyn.run(fmax=0.05)

print(f"Final Energy: {slab.get_potential_energy()} eV")
print(f"C-O Distance: {slab.cell[slab.indices.co[0], slab.indices.co[1]]}  Å")
