from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase import units

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()

opt = PreconLBFGS(atoms, precon='auto', trajectory='opt.traj')
opt.run(fmax=0.01)

print(f'Steps: {opt.nsteps}')
print(f'Energy: {atoms.get_potential_energy():.4f} eV')
cell_params = atoms.get_cell_lengths_and_angles()
print(f'Cell: a={cell_params[0]:.4f} Å, α={cell_params[3]:.2f}°')
