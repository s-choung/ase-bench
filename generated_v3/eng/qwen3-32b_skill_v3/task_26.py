from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.5, cubic=True)
atoms.calc = EMT()
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)
a, b, c, α, β, γ = atoms.get_cell_lengths_and_angles()
print(f"Steps: {opt.nsteps}")
print(f"Energy: {atoms.get_potential_energy()} eV")
print(f"Cell: {a:.3f} {b:.3f} {c:.3f} Å, {α:.2f} {β:.2f} {γ:.2f} deg")
