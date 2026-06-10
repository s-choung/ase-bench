import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS

a_values = np.linspace(3.45, 3.75, 9)
volumes, energies = [], []

for a in a_values:
    cu = bulk("Cu", "fcc", a=a, cubic=True)
    cu.calc = EMT()
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a_eq = v0 ** (1 / 3)

slab = fcc111("Cu", size=(2, 2, 4), a=a_eq, vacuum=10.0)
slab.calc = EMT()
slab_energy = slab.get_potential_energy()

co = Atoms("CO", positions=[(0, 0, 0), (0, 0, 1.15)])
co.center(vacuum=6.0)
co.calc = EMT()
BFGS(co, logfile=None).run(fmax=0.01)
co_energy = co.get_potential_energy()

z_cu = sorted(slab.positions[:, 2])
layers = []
for z in z_cu:
    if not layers or abs(z - layers[-1]) > 0.1:
        layers.append(z)
zcut = 0.5 * (layers[1] + layers[2])

add_adsorbate(slab, co, height=1.85, position="ontop", mol_index=0)
slab.set_constraint(FixAtoms(mask=[atom.symbol == "Cu" and atom.position[2] < zcut for atom in slab]))
slab.calc = EMT()

BFGS(slab, logfile=None).run(fmax=0.05)
adsorbed_energy = slab.get_potential_energy()
adsorption_energy = adsorbed_energy - slab_energy - co_energy

print(f"Equilibrium lattice constant: {a_eq:.6f} Angstrom")
print(f"Slab energy: {slab_energy:.6f} eV")
print(f"Adsorption energy: {adsorption_energy:.6f} eV")
