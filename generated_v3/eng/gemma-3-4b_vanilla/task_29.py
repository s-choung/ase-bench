from ase.md.verlet import VelocityVerlet
from ase.build import fcc211
from ase.calculators import EMT, LJ
from ase.io import write
from ase import units

def main():
    lattice = fcc211('Pd', a=3.824 Angstrom, size=(2, 2, 2))
    calc = EMT()
    lattice.set_calculator(calc)
    calc.xc = 'PBE'
    lattice.set_boundary('pccc')
    lattice.set_constraint('fixed', max_n=4)

    energies = []
    potential_energy = lattice.get_potential_energy()
    kinetic_energy = lattice.get_kinetic_energy()
    total_energy = potential_energy + kinetic_energy
    energies.append(total_energy)

    md = VelocityVerlet(lattice, dt=2.0 * units.fs)
    md.nsteps = 200
    md.temp = 500.0 * units.K
    md.run()

    final_total_energy = lattice.get_potential_energy() + lattice.get_kinetic_energy()
    energy_difference = final_total_energy - energies[0]
    print(f"Energy difference: {energy_difference:.6f}")

    write('Pd_NVE.traj', lattice)

if __name__ == '__main__':
    main()
