from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.calculators.lj import LJC
from ase.optimize import LBFGS
from ase.constraints import FixAtoms

calc = EMT(xc='pse', kpts=(2,2,2))
supercell = fcc111('Ni', size=(3, 3, 3), a=3.52)
supercell.set_calculator(calc)
calc.set_psp('pvxyz')
supercell.converge(mix_max=0.0, maxiter=100)

LJ = LJC(sigma=2.83)
supercell.set_calculator(LJ)

con = FixAtoms(indices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
supercell.set_constraint(con)

opt = LBFGS(selector=None, maxstep=0.05, trajectory='optimize.traj')
supercell.run(opt)

print("Number of steps:", opt.etime / opt.nelpa)
print("Final energy:", supercell.get_potential_energy())
print("Cell parameters:", supercell.lattice.a)
