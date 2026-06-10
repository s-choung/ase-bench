from ase import Atoms
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

a_initial = 3.6
atoms = Atoms('Cu', positions=[(0, 0, 0)], cell=[[0, a_initial/2, a_initial/2], 
                                               [a_initial/2, 0, a_initial/2], 
                                               [a_initial/2, a_initial/2, 0]], 
             pbc=True)
atoms *= (2, 2, 2)
atoms.calc = EMT()

energy_initial = atoms.get_potential_energy()
cell_initial = atoms.cell.cellpar()[:3]

print(f'Initial: Lattice constant = {a_initial:.3f} Å, Energy = {energy_initial:.3f} eV')

fc_filter = FrechetCellFilter(atoms)
opt = BFGS(fc_filter, logfile=None)
opt.run(fmax=0.01)

energy_final = atoms.get_potential_energy()
a_final = atoms.cell.cellpar()[0]

print(f'Final: Lattice constant = {a_final:.3f} Å, Energy = {energy_final:.3f} eV')
