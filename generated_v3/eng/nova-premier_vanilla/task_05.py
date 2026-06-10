from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', cubic=True)
vols, energies = [], []

for x in [0.95, 0.97, 1.0, 1.03, 1.05]:
    atoms.set_cell(atoms.cell * x, scale_atoms=True)
    atoms.calc = EMT()
    dyn = BFGS(atoms)
    dyn.run(fmax=0.001)
    vols.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(vols, energies)
v0, e0, B = eos.fit()
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B / 1e9:.2f} GPa")
