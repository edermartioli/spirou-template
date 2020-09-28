# spirou-template

`spirou-template` is a module to generate a SPIRou template spectrum out of a set of spectra from the same object.

To start using `spirou-template`, first make sure you have installed Python 3 via anaconda.

Then download all files in this repository and run the following example:

```
cd spirou-template/data/EpsEri/

python spirou_template.py --pattern=2*t.fits --rv_file=EpsEri.rdb --output=EpsEri_template.fits -pvn

```

Check if your results are similar to the template provided in the directory `expected_results`, or just compare the template with the one below:
