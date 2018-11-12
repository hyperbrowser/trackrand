#!/usr/bin/env python
import os.path
import argparse

from gtrackcore.input.userbins.UserBinSource import UserBinSource, GlobalBinSource
from gtrackcore.track.core.GenomeRegion import GenomeRegion
from gtrackcore.track.core.Track import Track, PlainTrack
from trackrand.utils.Constants import TRACK_NAME_SEP


def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument('-i', "--input", dest="inputFolder")
    argParser.add_argument("-g", "--genome", dest="genome")
    argParser.add_argument("-ra", "--randomization-algorithm", dest="randomizationAlg")
    argParser.add_argument("-o", "--output", dest="outputFolder")
    argParser.add_argument("-n", "--number-of-samples", dest="n", default=1)
    args = argParser.parse_args()

    inputFolderPath = args.inputFolder
    genome = args.genome

    os.path.walk(inputFolderPath, _handleFolder, 0)


def _handleFolder(_, dirName, fileNameList):
    for fileName in fileNameList:
        _handleFile(dirName, fileName)


def _handleFile(dirName, fileName):
    from gtrackcore.core import Api
    filePath = os.path.join(dirName, fileName)
    relFilePath = os.path.relpath(filePath)
    trackName = TRACK_NAME_SEP.join(os.path.normpath(relFilePath).split(os.sep))
    Api.importFile(filePath, "hg19", trackName)
    trackNameConverted = Api._convertTrackName(trackName)
    print trackName
    print trackNameConverted
    track = PlainTrack(trackNameConverted)
    # regionIter = UserBinSource('*','*','hg19')
    regionIter = GlobalBinSource("hg19")
    for region in regionIter:
        tv = track.getTrackView(region)
        print str(region)
        print tv.getNumElements()


if __name__ == '__main__':
    main()