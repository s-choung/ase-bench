from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.units import GPa
metals = ['Cu', 'Ag', 'Au']
initial_a = 4.0
results = []
for metal in metals:
    atoms = bulk(metal, 'fcc', a=initial_a, cubic=True)
    atoms.calc = EMT()
    eos = calculate_eos(atoms, eos='sj3', npoints=5)
    eos.fit()
    v0 = eos.v0
    a0 = v0 ** (1/3)
    B_GPa = eos.B * 1e9 / GPa
    results.append([metal, a0, B_GPa])
print('Metal    a0 (Å)    B (GPa)')
print('---------------------------')
for res in results:
    print(f'{res[0]:4} {res[1]:8.4f} {res[2]:10.2f}')
