from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

steps = opt.nsteps
energy = atoms.get_potential_energy()
cell = atoms.get_cell_lengths_and_angles()

print(f'Steps: {steps}')
print(f'Energy: {energy:.6f} eV')
print(f'Cell: {cell[0]:.4f} {cell[1]:.4f} {cell[2]:.4f} {cell[3]:.1f} {cell[4]:.1f} {cell[5]:.1f}')
