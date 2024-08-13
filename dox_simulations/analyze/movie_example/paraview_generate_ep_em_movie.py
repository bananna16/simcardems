# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10
import sys
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#file1 = "/Users/hermenegild/SSCP24_project/sscp_simcardems/demos/movie_example/IST_test/mechanics_u.xdmf"
file1 = "/Users/julebender/Documents/UNI/SummerSchool2024/Project/simcardems/dox_simulations/results/3DSlab/Results_Files/results_DOXM1_female_3D_10/mechanics_u.xdmf"
#file2 = "/Users/hermenegild/SSCP24_project/sscp_simcardems/demos/movie_example/IST_test/ep_V.xdmf"
file2 = "/Users/julebender/Documents/UNI/SummerSchool2024/Project/simcardems/dox_simulations/results/3DSlab/Results_Files/results_DOXM1_female_3D_10/ep_V.xdmf"
out = "{}.avi".format(file1)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1438, 1098]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [10.0, 3.5, 1.5]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [11.934388855123602, 33.09936750363098, -16.13499005021831]
renderView1.CameraFocalPoint = [6.966613879894997, -42.91585393318867, 29.154074776555806]
renderView1.CameraViewUp = [-0.015543933891199456, -0.5110217996433647, -0.8594271966888429]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 10.700467279516348
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1438, 1098)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Xdmf3ReaderS'
mechanics_uxdmf = Xdmf3ReaderS(registrationName='mechanics_u.xdmf', FileName=file1)

# create a new 'Xdmf3ReaderS'
ep_Vxdmf = Xdmf3ReaderS(registrationName='ep_V.xdmf', FileName=file2)

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(registrationName='ResampleWithDataset1', SourceDataArrays=ep_Vxdmf,
    DestinationMesh=mechanics_uxdmf)
resampleWithDataset1.CellLocator = 'Static Cell Locator'

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[mechanics_uxdmf, resampleWithDataset1])

# create a new 'Warp By Vector'
warpByVector1 = WarpByVector(registrationName='WarpByVector1', Input=appendAttributes1)
warpByVector1.Vectors = ['POINTS', 'u']

# create a new 'Annotate Time Filter'
#annotateTimeFilter1 = AnnotateTimeFilter(registrationName='AnnotateTimeFilter1', Input=warpByVector1)
#annotateTimeFilter1.Format = '{time:0.0f} ms'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from mechanics_uxdmf
mechanics_uxdmfDisplay = Show(mechanics_uxdmf, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
mechanics_uxdmfDisplay.Representation = 'Wireframe'
mechanics_uxdmfDisplay.AmbientColor = [0.0, 0.0, 0.0]
mechanics_uxdmfDisplay.ColorArrayName = ['POINTS', '']
mechanics_uxdmfDisplay.DiffuseColor = [0.0, 0.0, 0.0]
mechanics_uxdmfDisplay.SelectTCoordArray = 'None'
mechanics_uxdmfDisplay.SelectNormalArray = 'None'
mechanics_uxdmfDisplay.SelectTangentArray = 'None'
mechanics_uxdmfDisplay.OSPRayScaleArray = 'u'
mechanics_uxdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
mechanics_uxdmfDisplay.SelectOrientationVectors = 'u'
mechanics_uxdmfDisplay.ScaleFactor = 2.0
mechanics_uxdmfDisplay.SelectScaleArray = 'None'
mechanics_uxdmfDisplay.GlyphType = 'Arrow'
mechanics_uxdmfDisplay.GlyphTableIndexArray = 'None'
mechanics_uxdmfDisplay.GaussianRadius = 0.1
mechanics_uxdmfDisplay.SetScaleArray = ['POINTS', 'u']
mechanics_uxdmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
mechanics_uxdmfDisplay.OpacityArray = ['POINTS', 'u']
mechanics_uxdmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'
mechanics_uxdmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
mechanics_uxdmfDisplay.PolarAxes = 'PolarAxesRepresentation'
mechanics_uxdmfDisplay.ScalarOpacityUnitDistance = 2.7332896691039865
mechanics_uxdmfDisplay.OpacityArrayName = ['POINTS', 'u']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mechanics_uxdmfDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mechanics_uxdmfDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from warpByVector1
warpByVector1Display = Show(warpByVector1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'V'
vLUT = GetColorTransferFunction('V')
vLUT.AutomaticRescaleRangeMode = 'Never'
vLUT.RGBPoints = [-90.0, 0.02, 0.3813, 0.9981, -86.66666666666667, 0.02000006, 0.424267768, 0.96906969, -83.33333333333333, 0.02, 0.467233763, 0.940033043, -80.0, 0.02, 0.5102, 0.911, -76.66666666666667, 0.02000006, 0.546401494, 0.872669438, -73.33333333333334, 0.02, 0.582600362, 0.83433295, -70.0, 0.02, 0.6188, 0.796, -66.66666666666667, 0.02000006, 0.652535156, 0.749802434, -63.333333333333336, 0.02, 0.686267004, 0.703599538, -60.0, 0.02, 0.72, 0.6574, -56.66666666666667, 0.02000006, 0.757035456, 0.603735359, -53.33333333333333, 0.02, 0.794067037, 0.55006613, -50.0, 0.02, 0.8311, 0.4964, -46.666666666666664, 0.021354336738172372, 0.8645368555261631, 0.4285579460761159, -43.333333333333336, 0.023312914349117714, 0.897999359924484, 0.36073871343115577, -40.0, 0.015976108242848862, 0.9310479513349017, 0.2925631815088092, -36.66666666666667, 0.27421074700988196, 0.952562960995083, 0.15356836602739213, -33.333333333333336, 0.4933546281681699, 0.9619038625309482, 0.11119493614749336, -30.0, 0.6439, 0.9773, 0.0469, -26.666666666666664, 0.762401813, 0.984669591, 0.034600153, -23.333333333333343, 0.880901185, 0.992033407, 0.022299877, -20.0, 0.9995285432627147, 0.9995193706781492, 0.0134884641450013, -16.666666666666657, 0.999402998, 0.955036376, 0.079066628, -13.333333333333329, 0.9994, 0.910666223, 0.148134024, -10.0, 0.9994, 0.8663, 0.2172, -6.666666666666671, 0.999269665, 0.818035981, 0.217200652, -3.3333333333333286, 0.999133332, 0.769766184, 0.2172, 0.0, 0.999, 0.7215, 0.2172, 3.3333333333333286, 0.99913633, 0.673435546, 0.217200652, 6.666666666666671, 0.999266668, 0.625366186, 0.2172, 10.0, 0.9994, 0.5773, 0.2172, 13.333333333333343, 0.999402998, 0.521068455, 0.217200652, 16.666666666666657, 0.9994, 0.464832771, 0.2172, 20.0, 0.9994, 0.4086, 0.2172, 23.33333333333333, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206, 26.66666666666667, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934, 30.0, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357, 33.33333333333333, 0.949903037, 0.116867171, 0.252900603, 36.66666666666667, 0.903199533, 0.078432949, 0.291800389, 40.0, 0.8565, 0.04, 0.3307, 43.333333333333314, 0.798902627, 0.04333345, 0.358434298, 46.66666666666666, 0.741299424, 0.0466667, 0.386166944, 50.0, 0.6837, 0.05, 0.4139]
vLUT.ColorSpace = 'RGB'
vLUT.NanColor = [1.0, 0.0, 0.0]
vLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'V'
vPWF = GetOpacityTransferFunction('V')
vPWF.Points = [-90.0, 0.0, 0.5, 0.0, 50.0, 1.0, 0.5, 0.0]
vPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
warpByVector1Display.Representation = 'Surface'
warpByVector1Display.ColorArrayName = ['POINTS', 'V']
warpByVector1Display.LookupTable = vLUT
warpByVector1Display.SelectTCoordArray = 'None'
warpByVector1Display.SelectNormalArray = 'None'
warpByVector1Display.SelectTangentArray = 'None'
warpByVector1Display.OSPRayScaleArray = 'V'
warpByVector1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByVector1Display.SelectOrientationVectors = 'u'
warpByVector1Display.ScaleFactor = 1.741838836669922
warpByVector1Display.SelectScaleArray = 'None'
warpByVector1Display.GlyphType = 'Arrow'
warpByVector1Display.GlyphTableIndexArray = 'None'
warpByVector1Display.GaussianRadius = 0.0870919418334961
warpByVector1Display.SetScaleArray = ['POINTS', 'V']
warpByVector1Display.ScaleTransferFunction = 'PiecewiseFunction'
warpByVector1Display.OpacityArray = ['POINTS', 'V']
warpByVector1Display.OpacityTransferFunction = 'PiecewiseFunction'
warpByVector1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByVector1Display.PolarAxes = 'PolarAxesRepresentation'
warpByVector1Display.ScalarOpacityFunction = vPWF
warpByVector1Display.ScalarOpacityUnitDistance = 2.463936643862545
warpByVector1Display.OpacityArrayName = ['POINTS', 'V']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
warpByVector1Display.ScaleTransferFunction.Points = [32.394657135009766, 0.0, 0.5, 0.0, 40.74824523925781, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
warpByVector1Display.OpacityTransferFunction.Points = [32.394657135009766, 0.0, 0.5, 0.0, 40.74824523925781, 1.0, 0.5, 0.0]

# show data from annotateTimeFilter1
#annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
#annotateTimeFilter1Display.WindowLocation = 'Upper Center'
#annotateTimeFilter1Display.Color = [0.0, 0.0, 0.0]
#annotateTimeFilter1Display.FontSize = 25
#annotateTimeFilter1Display.ShowBorder = 'Always'

# setup the color legend parameters for each legend in this view

# get color legend/bar for vLUT in view renderView1
'''
vLUTColorBar = GetScalarBar(vLUT, renderView1)
vLUTColorBar.AutoOrient = 0
vLUTColorBar.Orientation = 'Horizontal'
vLUTColorBar.WindowLocation = 'Lower Center'
vLUTColorBar.Title = 'Transmembrane Potential (mV)'
vLUTColorBar.ComponentTitle = ''
vLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
vLUTColorBar.TitleFontSize = 25
vLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
vLUTColorBar.LabelFontSize = 20
vLUTColorBar.AutomaticLabelFormat = 0
vLUTColorBar.LabelFormat = '%2.0f'
vLUTColorBar.DrawTickMarks = 0
vLUTColorBar.DrawTickLabels = 0
vLUTColorBar.RangeLabelFormat = '%2.0f'
vLUTColorBar.ScalarBarThickness = 25


# set color bar visibility
vLUTColorBar.Visibility = 1

# show color legend
warpByVector1Display.SetScalarBarVisibility(renderView1, True)
'''

#center object 
renderView1.ResetCamera()

animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
#SetActiveSource(annotateTimeFilter1)
# ----------------------------------------------------------------

SaveAnimation(out, renderView1, ImageResolution=[1256, 560],
    FrameRate=50,
    FrameWindow=[0, 9990])

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
