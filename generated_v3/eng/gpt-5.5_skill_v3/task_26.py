from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize.precon import PreconLBFGS

atoms = bulk("Ni", "fcc", a=3.52, cubic=True)
atoms.calc = EMT()

filt = FrechetCellFilter(atoms)
opt = PreconLBFGS(filt, precon="auto", logfile=None)
opt.run(fmax=0.01)

cellpar = atoms.cell.cellpar()

print(f"Steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.8f} eV")
print(
    "Cell parameters: "
    f"a={cellpar[0]:.6f} Å, b={cellpar[1]:.6f} Å, c={cellpar[2]:.6f} Å, "
    f"alpha={cellpar[3]:.6f}°, beta={cellpar[4]:.6f}°, gamma={cellpar[5]:.6f}°"
)
