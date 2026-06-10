from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

Ni = bulk('Ni', 'fcc', a=3.5)
Ni.set_calculator(EMT(pseudopotentials={'Ni': '2p2s2d9q'}))
dyn = PreconLBFGS(Ni, precon='auto')
dyn.run(fmax=0.01)
print(f'Steps: {dyn.nsteps}')
print(f'Energy: {Ni.get_potential_energy():.6f} eV')
print(f'Cell: {Ni.get_cell()}')
