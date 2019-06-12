# Convgws
Python script to turn ascii point clouds into mCosmos .gws contour files or vice versa

Script uses argparse with the following options (available with convgws.py -h also)

indir (required) : path of file to be converted
outdir (optional) : path to save converted file (defaults to indir directory and tacks the converted file extension on the end)
view (optional) : [1,2,3] corresponding to XY(Z) (default), YZ(X), and ZX(Y)*

*Note the ToDo in convgws.py concerning "view". It does no conversion of the point index structure (i.e. XYZIJK -> YZXIJK). Currently, it only sticks that label into the .gws file.
