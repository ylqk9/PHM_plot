# utitlity functions
def PlotPHM(filename, phm_matrix = None, inverse = False, fmt = "pdf"):
	"""
	Given a particle-hole matrix or file, plot the particle-hole map.
	
	Parameters
	----------
	filename : file which contains the matrix of the particle-hole map or the file name to write the map.
	phm_matrix: the particle-hole matrix. It should be a numpy array
	inverse : turn the sign of the particle-hole map. (it is OK in the linear response theory).
	fmt: output format
	
	Returns
	-------
	no return. But there will be a new file named filename + '.pdf' which contains the plot in pdf format.
	"""
	try:
		phm = numpy.loadtxt(filename)
	except:
		if(type(phm_matrix) != None):
			phm = phm_matrix
		else:
			print("Error: please provide a file or a matrix as input")
	if(inverse): phm = -phm
	Lx = phm.shape[0]
	Ub = (numpy.ndarray.max(phm) + numpy.std(phm))/2
	#fig = pyplot.figure()
	cdict1 = {'red':  ((0.0, 1.0, 1.0), (0.5, 1.0, 1.0), (1.0, 0.0, 0.0)),
			'green': ((0.0, 0.0, 0.0), (0.5, 1.0, 1.0), (1.0, 0.0, 0.0)),
			'blue':  ((0.0, 0.0, 0.0), (0.5, 1.0, 1.0), (1.0, 1.0, 1.0))}
	phm_standard = LinearSegmentedColormap('PH_map_standard', cdict1)
	pyplot.imshow(phm, interpolation = 'none', extent = (0.5,Lx+0.5,0.5,Lx+0.5), cmap = phm_standard, vmin = -Ub, vmax = Ub, origin='lower')
	pyplot.colorbar()
	filenameext = filename.find(".")
	if(filenameext == -1):
		file = filename
	else:
		file = filename[:filenameext]
	file = file + "."
	try:
		pyplot.savefig(file + fmt)
		pyplot.close()
		print(file + fmt, " is saved.")
	except:
		print("Error: the format is not support by matplotlib")

