# spirou-template

`spirou-template` is a module to generate a SPIRou template spectrum out of a set of spectra for the same object.

To start using `spirou-template`, first make sure you have Python 3 installed via anaconda or if you have a custom installation of Python make sure you have all the dependencies installed.

Then download the files in this repository and run the following example:

```
cd spirou-template/data/EpsEri/

python ../../spirou_template.py --pattern=2*t.fits --rv_file=EpsEri.rdb --output=EpsEri_template.fits -pv
```

The following options are available:
```
--pattern for input data pattern (e.g., *e.fits or *t.fits)
--rv_file for input filename containing RV data for all input spectra
--output for output FITS filename to save final template spectrum
-p for plotting
-v for verbose
-m to combine by median instead of mean
-n to normalize final template by continuum
```
Notice that we provide the file `EpsEri.rdb` containing the source radial velocities for the spectra in `data/EpsEri/*t.fits`, which have been measured using the CCF method. To calculate the template for a different set of files, one needs to calculate the RVs first and build a new `.rdb` file. The units in the`.rdb` file are RJD=BJD-2400000 and km/s.

One can check if the results are similar to the template provided in the directory `data/EpsEri/TEMPLATES/`, or just compare the plot below:

![Alt text](Figures/EpsEri.png?raw=true "Title")

Figure above presents the final template spectrum in red, and in blue are the input spectra and residuals (I suggest one to zoom in to see these details when displaying with the pyplot window). The green curves show the +/- 3 x sigma, where sigma is given by the standard deviation between all input spectra.  
