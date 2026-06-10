from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()

filt = FrechetCellFilter(atoms)
opt = PreconLBFGS(filt, precon='auto', logfile=None)
opt.run(fmax=0.01)

energy = atoms.get_potential_energy()
cellpar = atoms.cell.cellpar()

print(f"steps: {opt.nsteps}")
print(f"final energy: {energy:.6f} eV")
print("cell parameters (a, b, c, alpha, beta, gamma):",
      " ".join(f"{x:.6f}" for x in cellpar))
