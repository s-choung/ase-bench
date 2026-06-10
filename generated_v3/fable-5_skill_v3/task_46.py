from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

n_slab = len(slab) - 2
i_c, i_o = n_slab, n_slab + 1

c1 = FixAtoms(mask=[a.tag == 3 for a in slab])
c2 = FixBondLength(i_c, i_o)
slab.set_constraint([c1, c2])

slab.calc = EMT()
BFGS(slab, trajectory='opt.traj').run(fmax=0.05)

print(f"Final energy: {slab.get_potential_energy():.4f} eV")
print(f"C-O distance: {slab.get_distance(i_c, i_o):.4f} Å")
