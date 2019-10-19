#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
A solar system simulation
'''
import planets.mars


def main():
    '''
    Start the simulation...
    '''
    print('Simulation...')
    print("Aphelion: {}".format(planets.mars.APHELION_KM))
    print("Perihelion: {}".format(planets.mars.PERIHELION_KM))
    print("Semi-major axis: {}".format(planets.mars.SEMI_MAJOR_AXIS_KM))


if __name__ in '__main__':
    main()
