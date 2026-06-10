from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.build import bulk

atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

print(f'Steps: {opt.nsteps}')
print(f'Energy: {atoms.get_potential_energy():.5f} eV')
cell = atoms.get_cell()
print(f'Cell [Å]\n{cell}')
