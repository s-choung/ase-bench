from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
c = add_adsorbate(slab, 'CO', height=2.0, position='ontop')

fix_bottom = FixAtoms(mask=[atom.tag == 1 for atom in slab])
fix_co = FixBondLength(atoms=c, bond_length=1.13)

c.set_constraint(fix_bottom)
c.set_constraint(fix_co)

calc = EMT()
c.calc = calc

c.get_potential_energy()
print("Initial energy:", c.get_potential_energy())

opt = BFGS(c, trajectory='co_on_pt.traj')
opt.run(fmax=0.05)

print("Final energy:", c.get_potential_energy())
print("C-O distance:", c.get_distance('CO'))
