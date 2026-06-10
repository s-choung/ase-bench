from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)
atoms.calc = EMT()

opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

print(f"Steps: {opt.get_number_of_steps()}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")
a, b, c, alpha, beta, gamma = atoms.get_cell_lengths_and_angles()
print(f"Cell: a={a:.4f} b={b:.4f} c={c:.4f} alpha={alpha:.2f} beta={beta:.2f} gamma={gamma:.2f}")
