from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT(precon='auto')
opt = PreconLBFGS(FrechetCellFilter(atoms))
nsteps = opt.run(fmax=0.01)
energy = atoms.get_potential_energy()
cell = atoms.get_cell_lengths_and_angles()
print(f'Steps: {nsteps}')
print(f'Final energy: {energy:.6f} eV')
print(f'Cell (a,b,c,alpha,beta,gamma): {cell}')
