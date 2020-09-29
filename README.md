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
-p for plotting
-v for verbose
-m to combine by median instead of mean
-n to normalize final template by continuum
```

Check if your results are similar to the template provided in the directory `EpsEri/TEMPLATES/`, or just compare the plot below:


