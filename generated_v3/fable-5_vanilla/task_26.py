from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.6, cubic=True)
atoms.rattle(stdev=0.05, seed=42)
atoms.calc = EMT()

opt = PreconLBFGS(atoms, precon='auto', variable_cell=True)
opt.run(fmax=0.01)

print(f"Steps: {opt.get_number_of_steps()}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell parameters: {atoms.cell.cellpar()}")
