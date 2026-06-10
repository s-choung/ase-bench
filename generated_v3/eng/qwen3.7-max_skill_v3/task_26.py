from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

opt = PreconLBFGS(FrechetCellFilter(atoms), precon='auto')
opt.run(fmax=0.01)

a, b, c, alpha, beta, gamma = atoms.get_cell_lengths_and_angles()
print(f"Steps: {opt.nsteps}")
print(f"Final Energy: {atoms.get_potential_energy():.4f} eV")
print(f"Cell parameters: a={a:.4f}, b={b:.4f}, c={c:.4f}, α={alpha:.2f}, β={beta:.2f}, γ={gamma:.2f}")
