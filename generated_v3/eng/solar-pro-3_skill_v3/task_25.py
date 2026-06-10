from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# bulk Cu FCC, initial lattice constant
a_init = 3.6  # Å
atoms = bulk('Cu', 'fcc', a=a_init)
atoms.calc = EMT()

# before optimization
cell_before = atoms.get_cell()
E_before = atoms.get_potential_energy()

print('Before:  a = {:.3f} Å, E = {:.6f} eV'.format(cell_before[0], E_before))

# optimization with FrechetCellFilter
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# after optimization
a_final = atoms.get_cell()[0]
E_final = atoms.get_potential_energy()
cell_final = atoms.get_cell()

print('After:   a = {:.3f} Å, E = {:.6f} eV'.format(a_final, E_final))

# optional: print relative changes
print('Δa = {:.3f} Å, ΔE = {:.6f} eV'.format(a_final - a_init, E_final - E_before))
