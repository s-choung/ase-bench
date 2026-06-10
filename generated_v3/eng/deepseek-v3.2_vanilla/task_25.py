from ase import Atoms
from ase.optimize import BFGS
from ase.constraints import UnitCellFilter
from ase.calculators.emt import EMT

# Create initial FCC Cu structure
a_initial = 3.6  # Initial lattice constant
atoms = Atoms('Cu', positions=[[0, 0, 0]], cell=[[0, a_initial/2, a_initial/2],
                                                 [a_initial/2, 0, a_initial/2],
                                                 [a_initial/2, a_initial/2, 0]],
              pbc=True)
atoms *= (2, 2, 2)  # 2x2x2 supercell
atoms.calc = EMT()

print(f'Initial: cell size = {atoms.cell.lengths()}, energy = {atoms.get_potential_energy():.6f} eV')

# Optimize using FrechetCellFilter (UnitCellFilter with hydrostatic strain)
ucf = UnitCellFilter(atoms, hydrostatic_strain=True)
opt = BFGS(ucf)
opt.run(fmax=0.01)

print(f'Final:   cell size = {atoms.cell.lengths()}, energy = {atoms.get_potential_energy():.6f} eV')
