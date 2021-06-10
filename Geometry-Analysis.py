import os
import numpy
import argparse

def calculate_distance(coords1, coords2):
    x = coords1[0] - coords2[0]
    y = coords1[1] - coords2[1]
    z = coords1[2] - coords2[2]
    distance = numpy.sqrt(x**2 + y**2 + z**2)
    return distance

def bond_check(distance, minimum=0, maximum=1.5):
    """
    Checks if a distance is a bond based on a minimum and a maximum
    Inputs: distance, minimum length for bond, maximum length for bond
    Defaults: minimum: 0 angstroms, maximum: 1.5 angstroms
    """
    if distance > minimum and distance < maximum:
        return True
    else:
        return False

def open_xyz(filepath):
    """
    This function opens a standard xyz file.
    It returns the atoms as strings and the coordinates as floats.
    """
    data = numpy.genfromtxt(fname=filepath, dtype='unicode', skip_header=2)
    atoms = data[:,0]
    coordinates = data[:, 1:]
    coordinates = coordinates.astype(float)
    return atoms, coordinates

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description ="The script analyzes a user given xyz file and outputs the lengths of all the bonds.")
    parser.add_argument('xyz_file', help='The filepath of the xyz file to analyze.')
    args = parser.parse_args()

    file_location = args.xyz_file
    atoms, coordinates = open_xyz(file_location) 
    num_atoms = len(atoms)
    for num1 in range(0, num_atoms):
        for num2 in range(num1, num_atoms):
            distance = calculate_distance(coordinates[num1], coordinates[num2])
            if bond_check(distance) is True:
                print(F'{atoms[num1]} to {atoms[num2]} : {distance:.3f}')