from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

ni = bulk('Ni', 'fcc', a=3.52, cubic=True)
ni.calc = EMT()
opt = PreconLBFGS(ni, precon='auto')
opt.run(fmax=0.01)

print(f"Steps: {opt.nsteps}")
print(f"Energy: {ni.get_potential_energy():.3f} eV")
print(f"Cell: {ni.cell.cellpar()}")
