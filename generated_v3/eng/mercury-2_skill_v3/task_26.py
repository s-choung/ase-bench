from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

print('steps:', opt.nsteps)
print('energy (eV):', atoms.get_potential_energy())
print('cell (a,b,c,α,β,γ):', atoms.get_cell_lengths_and_angles())
