# -*- coding: iso-8859-1 -*-
"""
    Created on Sep 28 2020
    
    Description: This routine builds a template spectrum out of a list of input SPIRou spectra
    
    @author: Eder Martioli <martioli@iap.fr>
    
    Institut d'Astrophysique de Paris, France.

    Simple usage example:
    
    python spirou_template.py --pattern=*t.fits --rv_file=EpsEri.rdb --output=EpsEri_template.fits -vp
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

from optparse import OptionParser
import os,sys

import numpy as np
import glob

import astropy.io.fits as fits
import spiroulib

parser = OptionParser()
parser.add_option("-t", "--pattern", dest="pattern", help="Spectral data pattern",type='string',default="*t.fits")
parser.add_option("-r", "--rv_file", dest="rv_file", help="RV file name (*.rdb)",type='string',default="")
parser.add_option("-o", "--output", dest="output", help="Output template file",type='string', default="")
parser.add_option("-n", action="store_true", dest="normalize", help="normalize", default=False)
parser.add_option("-m", action="store_true", dest="median", help="median", default=False)
parser.add_option("-v", action="store_true", dest="verbose", help="verbose", default=False)
parser.add_option("-p", action="store_true", dest="plot", help="plot", default=False)

try:
    options,args = parser.parse_args(sys.argv[1:])
except:
    print("Error: check usage with spirou_template.py -h ")
    sys.exit(1)

if options.verbose:
    print('Spectral data pattern: ', options.pattern)
    print('RV file name: ', options.rv_file)
    print('Output: ', options.output)
    print('Combine by median?: ', options.median)
    print('Normalize by continuum?: ', options.normalize)

# make list of data files
if options.verbose:
    print("Creating list of spectrum files...")
inputdata = sorted(glob.glob(options.pattern))
#---

master_spectrum = spiroulib.template_using_fit(inputdata, options.rv_file, median=options.median, normalize_by_continuum=options.normalize, verbose=options.verbose, plot=options.plot)

if options.output != "" :
    spiroulib.write_spectrum_to_fits(master_spectrum, options.output, header=fits.getheader(inputdata[0]), wavekey='wl_template', fluxkey='flux_template', fluxerrkey='fluxerr_template')
