cwDir = "localhost:/projects/daby8982/Week10/Week10_Datasets/"

def openDatafile(fName):
	OpenDatabase(cwDir + fName)

def insertImageBackground():
	OpenDatabase("localhost:/projects/daby8982/Week10/Week10_Datasets/katrinaTerrain.png", 0)
	AddPlot("Truecolor", "color")
	SetActivePlots(4)
	AddOperator("Elevate", 0)
	ElevateAtts = ElevateAttributes()
	ElevateAtts.useXYLimits = 0
	ElevateAtts.limitsMode = ElevateAtts.OriginalData  # OriginalData, CurrentPlot
	ElevateAtts.scaling = ElevateAtts.Linear  # Linear, Log, Skew
	ElevateAtts.skewFactor = 1
	ElevateAtts.minFlag = 0
	ElevateAtts.min = 0
	ElevateAtts.maxFlag = 0
	ElevateAtts.max = 1
	ElevateAtts.zeroFlag = 1
	ElevateAtts.variable = "default"
	SetOperatorOptions(ElevateAtts, 0)
	AddOperator("Transform", 0)
	TransformAtts = TransformAttributes()
	TransformAtts.doScale = 1
	TransformAtts.scaleX = 0.429
	TransformAtts.scaleY = 0.681
	SetOperatorOptions(TransformAtts, 0)

def createWindVectors():
	DefineVectorExpression("wind", "{U, V, W}")
	DefineScalarExpression("windMag", "magnitude(wind)")

def createWindStreamlines():
	AddPlot("Streamline", "wind")
	StreamlineAtts = StreamlineAttributes()
	StreamlineAtts.sourceType = StreamlineAtts.SpecifiedCircle  # SpecifiedPoint, SpecifiedPointList, SpecifiedLine, SpecifiedCircle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection
	StreamlineAtts.planeOrigin = (165, 138, 5)
	StreamlineAtts.planeNormal = (0, 0, 1)
	StreamlineAtts.planeUpAxis = (0, 1, 0)
	StreamlineAtts.radius = 100
	StreamlineAtts.sampleDensity0 = 5
	StreamlineAtts.sampleDensity1 = 4
	StreamlineAtts.sampleDensity2 = 2
	StreamlineAtts.coloringMethod = StreamlineAtts.ColorByVariable  # Solid, ColorBySpeed, ColorByVorticity, ColorByLength, ColorByTime, ColorBySeedPointID, ColorByVariable, ColorByCorrelationDistance, ColorByNumberDomainsVisited
	StreamlineAtts.colorTableName = "hot"
	StreamlineAtts.integrationDirection = StreamlineAtts.Both  # Forward, Backward, Both
	StreamlineAtts.maxTimeStep = 0.01
	StreamlineAtts.coloringVariable = "windMag"
	StreamlineAtts.displayMethod = StreamlineAtts.Tubes  # Lines, Tubes, Ribbons
	StreamlineAtts.tubeRadiusBBox = 0.004
	StreamlineAtts.varyTubeRadius = StreamlineAtts.Scalar  # None, Scalar
	StreamlineAtts.varyTubeRadiusFactor = 4
	StreamlineAtts.varyTubeRadiusVariable = "windMag"
	SetPlotOptions(StreamlineAtts)

def createClouds():
	AddPlot("Volume", "QCLOUD")
	SetActivePlots(1)
	AddOperator("Transform", 0)
	TransformAtts = TransformAttributes()
	TransformAtts.doScale = 1
	TransformAtts.scaleZ = 3
	SetOperatorOptions(TransformAtts, 0)

	### Transfer Function to 'xray' color table
	VolumeAtts = VolumeAttributes()
	VolumeAtts.legendFlag = 1
	VolumeAtts.lightingFlag = 1
	VolumeAtts.colorControlPoints.GetControlPoints(0).colors = (255, 255, 255, 255)
	VolumeAtts.colorControlPoints.GetControlPoints(0).position = 0
	VolumeAtts.colorControlPoints.GetControlPoints(1).colors = (0, 0, 0, 255)
	VolumeAtts.colorControlPoints.GetControlPoints(1).position = 1
	VolumeAtts.colorControlPoints.smoothing = VolumeAtts.colorControlPoints.Linear  # None, Linear, CubicSpline
	VolumeAtts.colorControlPoints.equalSpacingFlag = 0
	VolumeAtts.colorControlPoints.discreteFlag = 0
	VolumeAtts.colorControlPoints.categoryName = ""
	VolumeAtts.opacityAttenuation = 1
	VolumeAtts.opacityMode = VolumeAtts.FreeformMode  # FreeformMode, GaussianMode, ColorTableMode
	#controlPoints does not contain any GaussianControlPoint objects.
	VolumeAtts.resampleFlag = 1
	VolumeAtts.resampleTarget = 500000
	VolumeAtts.opacityVariable = "default"
	VolumeAtts.compactVariable = "default"
	VolumeAtts.useColorVarMin = 0
	VolumeAtts.colorVarMin = 0
	VolumeAtts.useColorVarMax = 0
	VolumeAtts.colorVarMax = 0
	VolumeAtts.useOpacityVarMin = 0
	VolumeAtts.opacityVarMin = 0
	VolumeAtts.useOpacityVarMax = 0
	VolumeAtts.opacityVarMax = 0
	VolumeAtts.smoothData = 0
	VolumeAtts.samplesPerRay = 500
	VolumeAtts.rendererType = VolumeAtts.Splatting  # Splatting, Texture3D, RayCasting, RayCastingIntegration, SLIVR, RayCastingSLIVR, Tuvok
	VolumeAtts.gradientType = VolumeAtts.SobelOperator  # CenteredDifferences, SobelOperator
	VolumeAtts.num3DSlices = 200
	VolumeAtts.scaling = VolumeAtts.Linear  # Linear, Log, Skew
	VolumeAtts.skewFactor = 1
	VolumeAtts.limitsMode = VolumeAtts.OriginalData  # OriginalData, CurrentPlot
	VolumeAtts.sampling = VolumeAtts.Rasterization  # KernelBased, Rasterization, Trilinear
	VolumeAtts.rendererSamples = 3
	#transferFunction2DWidgets does not contain any TransferFunctionWidget objects.
	VolumeAtts.transferFunctionDim = 1
	VolumeAtts.lowGradientLightingReduction = VolumeAtts.Lower  # Off, Lowest, Lower, Low, Medium, High, Higher, Highest
	VolumeAtts.lowGradientLightingClampFlag = 0
	VolumeAtts.lowGradientLightingClampValue = 1
	VolumeAtts.materialProperties = (0.4, 0.75, 0, 15)
	SetPlotOptions(VolumeAtts)

def createHotTowers():
	AddPlot("Pseudocolor", "QCLOUD")
	SetActivePlots(2)
	AddOperator("Transform", 0)
	TransformAtts = TransformAttributes()
	TransformAtts.doScale = 1
	TransformAtts.scaleZ = 3
	SetOperatorOptions(TransformAtts, 0)
	AddOperator("Isovolume", 0)
	IsovolumeAtts = IsovolumeAttributes()
	IsovolumeAtts.lbound = 0.0005
	SetOperatorOptions(IsovolumeAtts, 0)
	PseudocolorAtts = PseudocolorAttributes()
	PseudocolorAtts.maxFlag = 1
	PseudocolorAtts.max = 0.0015
	PseudocolorAtts.colorTableName = "Reds"
	PseudocolorAtts.legendFlag = 0
	SetPlotOptions(PseudocolorAtts)

def createRainfall():
	AddPlot("Pseudocolor", "RAINNC")
	SetActivePlots(3)
	AddOperator("Elevate", 0)
	ElevateAtts = ElevateAttributes()
	ElevateAtts.zeroFlag = 1
	SetOperatorOptions(ElevateAtts, 0)
	AddOperator("Transform", 0)
	TransformAtts = TransformAttributes()
	TransformAtts.doTranslate = 1
	TransformAtts.translateZ = 0.05
	SetOperatorOptions(TransformAtts, 0)
	AddOperator("Isovolume", 0)
	IsovolumeAtts = IsovolumeAttributes()
	IsovolumeAtts.lbound = 15
	SetOperatorOptions(IsovolumeAtts, 0)

def createView():
	View3DAtts = View3DAttributes()
	View3DAtts.viewNormal = (-0.509478, -0.816541, 0.271466)
	View3DAtts.focus = (219.648, 261.504, 49.5)
	View3DAtts.viewUp = (0.0455888, 0.289424, 0.956115)
	View3DAtts.viewAngle = 30
	View3DAtts.parallelScale = 345.079
	View3DAtts.nearPlane = -690.159
	View3DAtts.farPlane = 690.159
	View3DAtts.imagePan = (0, 0)
	View3DAtts.imageZoom = 1.77156
	View3DAtts.perspective = 1
	View3DAtts.eyeAngle = 2
	View3DAtts.centerOfRotationSet = 0
	View3DAtts.centerOfRotation = (219.648, 261.504, 49.5)
	View3DAtts.axis3DScaleFlag = 0
	View3DAtts.axis3DScales = (1, 1, 1)
	View3DAtts.shear = (0, 0, 1)
	View3DAtts.windowValid = 1
	SetView3D(View3DAtts)

def addLight():
	light0 = LightAttributes()
	light0.enabledFlag = 1
	light0.type = light0.Camera  # Ambient, Object, Camera
	light0.direction = (0, 0, -1)
	light0.color = (255, 255, 255, 255)
	light0.brightness = 1
	SetLight(0, light0)
	light1 = LightAttributes()
	light1.enabledFlag = 1
	light1.type = light1.Object  # Ambient, Object, Camera
	light1.direction = (0, 0, -1)
	light1.color = (255, 255, 255, 255)
	light1.brightness = 0.65
	SetLight(1, light1)

def createAnnotations():
	AnnotationAtts = AnnotationAttributes()
	AnnotationAtts.axes3D.visible = 0
	AnnotationAtts.axes3D.triadFlag = 0
	AnnotationAtts.axes3D.bboxFlag = 0
	AnnotationAtts.backgroundColor = (0, 0, 0, 255)
	SetAnnotationAttributes(AnnotationAtts)

def saveImage(fName):
	SaveWindowAtts = SaveWindowAttributes()
	SaveWindowAtts.outputDirectory = "localhost:/projects/daby8982/Week10/"
	SaveWindowAtts.fileName = fName
	SaveWindowAtts.format = SaveWindowAtts.PNG
	SaveWindowAtts.width = 1024
	SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions
	SetSaveWindowAttributes(SaveWindowAtts)
	SaveWindow()

'''
def createPressureTemperature():
	AddPlot("Pseudocolor", "P")
	SetActivePlots(0)
	SetActivePlots(0)
	AddOperator("Isosurface")
	IsosurfaceAtts = IsosurfaceAttributes()
	IsosurfaceAtts.contourValue = (10)
	IsosurfaceAtts.contourMethod = IsosurfaceAtts.Value  # Level, Value, Percent
	IsosurfaceAtts.variable = "T"
	SetOperatorOptions(IsosurfaceAtts, 1)
	PseudocolorAtts = PseudocolorAttributes()
	PseudocolorAtts.colorTableName = "hot_and_cold"
	PseudocolorAtts.opacityType = PseudocolorAtts.Constant  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
	PseudocolorAtts.opacityVariable = ""
	PseudocolorAtts.opacity = 0.20
	SetPlotOptions(PseudocolorAtts)

def createSeaTemperature():
	ActivateDatabase("localhost:/projects/daby8982/Week10/Week10_Datasets/wrfout_d02_2005-08-29_07")
	AddPlot("Pseudocolor", "SST", 1, 0)
	AddOperator("Elevate", 0)
	SetActivePlots(2)
	AddOperator("Transform", 0)
	TransformAtts.scaleX = 0.713
	TransformAtts.scaleY = 0.587
	TransformAtts.scaleZ = 0.001
	SetOperatorOptions(TransformAtts, 0)

def createWindVectorField():
	AddPlot("Vector", "wind", 1, 0)
	SetActivePlots(3)
	AddOperator("Slice", 0)
	SliceAtts = SliceAttributes()
	SliceAtts.originType = SliceAtts.Intercept  # Point, Intercept, Percent, Zone, Node
	SliceAtts.originIntercept = 5
	SliceAtts.axisType = SliceAtts.ZAxis  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
	SetOperatorOptions(SliceAtts, 0)
	VectorAtts = VectorAttributes()
	VectorAtts.nVectors = 2500
	VectorAtts.lineStyle = VectorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	VectorAtts.lineWidth = 2
	VectorAtts.scale = 0.25
	VectorAtts.headSize = 0.5
	VectorAtts.headOn = 1
	VectorAtts.colorByMag = 1
	VectorAtts.vectorOrigin = VectorAtts.Tail  # Head, Middle, Tail
	VectorAtts.glyphType = VectorAtts.Arrow  # Arrow, Ellipsoid
	SetPlotOptions(VectorAtts)
'''

###############
# Main
###############

openDatafile("wrfout_d02_2005-08-29_07.nc")
createWindVectors()
createWindStreamlines()
createClouds()
createHotTowers()
createRainfall()
addLight()
insertImageBackground()
createView()
createAnnotations()
DrawPlots()
saveImage("katrina_finalPlate")
