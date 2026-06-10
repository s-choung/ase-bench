from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', cubic=False)
volumes = []
energies = []
for scale in [0.95, 0.97, 0.99, 1.01, 1.03, 1.05]:
    au = atoms.copy()
    au.set_cell(au.cell * scale**(1/3), scale_atoms=True)
    au.calc = EMT()
    volumes.append(au.get_volume())
    energies.append(au.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, bulk_mod = eos.fit()
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {bulk_mod:.3f} eV/Å³")
