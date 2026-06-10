from ase import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

opt = PreconLBFGS(FrechetCellFilter(atoms), precon='auto')
opt.run(fmax=0.01)

steps = opt.get_number_of_steps()
energy = atoms.get_potential_energy()
cell_params = atoms.get_cell_lengths_and_angles()

print(f'Steps: {steps}')
print(f'Final energy: {energy:.6f} eV')
print(f'Cell parameters: {cell_params}')
