from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk("Cu", "fcc", a=3.8, cubic=True)
atoms.calc = EMT()

def show(label):
    print(label)
    print("Cell:")
    print(atoms.cell)
    print("Cell lengths:", atoms.cell.lengths())
    print("Energy:", atoms.get_potential_energy(), "eV")

show("Before optimization:")

cell_filter = FrechetCellFilter(atoms)
opt = BFGS(cell_filter, logfile=None)
opt.run(fmax=0.01)

show("After optimization:")
