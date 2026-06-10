from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT(precon='auto')
opt = PreconLBFGS(FrechetCellFilter(atoms), logfile=None)
n_steps = opt.run(fmax=0.01)
print(f'Steps: {n_steps}')
print(f'Energy: {atoms.get_potential_energy():.6f} eV')
a, b, c, alpha, beta, gamma = atoms.get_cell_lengths_and_angles()
print(f'Cell: a={a:.4f} Å, b={b:.4f} Å, c={c:.4f} Å')
print(f'Angles: α={alpha:.2f}°, β={beta:.2f}°, γ={gamma:.2f}°')
