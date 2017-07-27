#include <stdio.h>
#include <stdlib.h>
#include <osgViewer/Viewer>
#include <osgDB/ReadFile>

int main(int argc, char *argv[])
{
    osgViewer::Viewer viewer;
    osg::Node* node = osgDB::readNodeFile("D:/SXEarth3.4.1/data/airport/nanyuan.ive");

    viewer.setSceneData(node);
    viewer.run();
    return 0;
}
