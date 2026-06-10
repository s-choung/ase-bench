from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, crystalstructure='fcc', a=4.0)
    atoms.calc = EMT()

    volumes = []
    energies = []

    for x in [0.95, 1.0, 1.05]:
        a = atoms.copy()
        a.set_cell(a.get_cell() * x, scale_atoms=True)
        energies.append(a.get_potential_energy())
        volumes.append(a.get_volume())

    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()

    results.append({'Metal': metal, 'a_eq': v0**(1/3), 'B': B})

# Print the results in a comparison table format
print("{:<5} {:<15} {:<15}".format('Metal', 'a_eq (Å)', 'B (GPa)'))
print("-"*30)
for result in results:
    print("{:<5} {:<15.3f} {:<15.1f}".format(result['Metal'], result['a_eq'], result['B'] / 1E5))
