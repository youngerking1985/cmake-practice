#include <stdio.h>
#include <stdlib.h>
#include <osgViewer/Viewer>
#include <osgDB/ReadFile>
#include <osgEarthUtil/EarthManipulator>

int main(int argc, char *argv[])
{
    osgViewer::Viewer viewer;
    osg::Node* node = osgDB::readNodeFile("D:/srccode/osgearth-2.8/tests/gdal_tiff.earth");
    // osg::Node* node = osgDB::readNodeFile("D:/SXEarth3.4.1/data/airport/nanyuan.ive");

    viewer.setSceneData(node);
    viewer.setCameraManipulator(new osgEarth::Util::EarthManipulator);
    viewer.run();
    return 0;
}
