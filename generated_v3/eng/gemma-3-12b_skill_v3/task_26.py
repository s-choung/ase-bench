from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
import ase

atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT(precon='auto')

opt = PreconLBFGS(atoms, trajectory='ni_fcc_emt.traj')
opt.run(fmax=0.01)

print("Number of steps:", opt.n_steps)
print("Final energy:", atoms.get_potential_energy())
print("Final cell parameters:", atoms.get_cell_lengths_and_angles())
