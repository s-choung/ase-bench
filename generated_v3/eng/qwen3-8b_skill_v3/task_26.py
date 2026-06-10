from ase import Atoms
from ase.build import bulk
from ase.optimize.precon import PreconLBFGS
from ase.calculators.emt import EMT

atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)
atoms.calc = EMT()
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)
print(f"Steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy()}")
print(f"Cell parameters: {atoms.get_cell()}")
