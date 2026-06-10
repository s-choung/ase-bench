from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(4, 4, 3), vacuum=10.0)
co = add_adsorbate(slab, 'CO', height=2.0, position='ontop')

mask = [atom.tag > 2 for atom in slab]
constraint1 = FixAtoms(mask=mask)

constraint2 = FixBondLength(0, 1)

co.set_constraint(constraint1)
co.set_constraint(constraint2)

calc = EMT()
co.calc = calc

dyn = BFGS(co, trajectory='co_pt.traj', logfile='co_pt.log')
dyn.run(fmax=0.05)

print(f"Final energy: {co.get_potential_energy():.5f} eV")
print(f"C-O distance: {co.get_distances()[0, 1]:.4f} Angstrom")
