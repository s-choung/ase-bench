from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)
atoms.calc = EMT()

opt = PreconLBFGS(atoms, precon='auto', trajectory='ni_opt.traj')
opt.run(fmax=0.01)

print("steps =", opt.nsteps)
print("final_energy_eV =", atoms.get_potential_energy())
print("cell_parameter_A =", atoms.cell.lengths()[0])
