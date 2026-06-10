from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.6)
atoms.calc = EMT()
opt = PreconLBFGS(FrechetCellFilter(atoms), precon='auto')
nsteps = opt.run(fmax=0.01)
e_final = atoms.get_potential_energy()
cell_params = atoms.get_cell_lengths_and_angles()
a, b, c = cell_params[:3]

print(f"Optimization steps: {nsteps}")
print(f"Final energy: {e_final:.4f} eV")
print(f"Cell lengths (Å): a={a:.4f}, b={b:.4f}, c={c:.4f}")
