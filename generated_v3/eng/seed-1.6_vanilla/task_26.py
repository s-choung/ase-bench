from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

atoms = bulk('Ni', 'fcc')
atoms.calc = EMT()
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

print(f'Steps: {opt.get_number_of_steps()}')
print(f'Final energy: {atoms.get_potential_energy():.6f} eV')
print(f'Cell parameters: {atoms.get_cell_params():.6f} Å')
