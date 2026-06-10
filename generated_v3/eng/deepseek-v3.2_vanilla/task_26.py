from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = Atoms('Ni', cell=[(0, 2.0, 2.0), (2.0, 0, 2.0), (2.0, 2.0, 0)], pbc=True)
atoms *= (2, 2, 2)
atoms.calc = EMT()

opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

print(f'Steps: {opt.get_number_of_steps()}')
print(f'Final energy: {atoms.get_potential_energy():.6f} eV')
print('Cell parameters:')
print(atoms.cell[:])
