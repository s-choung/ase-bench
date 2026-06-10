from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.set_calculator(EMT())

opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

print('Steps:', opt.nsteps)
print('Energy (eV):', atoms.get_potential_energy())
print('Cell (Å):', atoms.get_cell())
