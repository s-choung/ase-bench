from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase.constraints import UnitCellFilter

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()

ucf = UnitCellFilter(atoms)
dyn = PreconLBFGS(ucf, precon='auto')
dyn.run(fmax=0.01)

print(f"Number of steps: {dyn.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell parameter: {atoms.cell[0, 0]:.6f} Å")
