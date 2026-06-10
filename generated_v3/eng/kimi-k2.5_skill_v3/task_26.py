from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)
atoms.calc = EMT()
opt = PreconLBFGS(FrechetCellFilter(atoms), precon='auto')
nsteps = opt.run(fmax=0.01)
print(f"Steps: {nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
c = atoms.get_cell_lengths_and_angles()
print(f"Cell: a={c[0]:.4f} Å, b={c[1]:.4f} Å, c={c[2]:.4f} Å, α={c[3]:.2f}°, β={c[4]:.2f}°, γ={c[5]:.2f}°")
