import os

from gtrackcore.track.core.Track import PlainTrack
from temp.gtrackcore.track.core.TrackStructure import TrackStructureV2, SingleTrackTS
from trackrand.utils.Constants import TRACK_NAME_SEP


def createTrackFromFile(dirname, filename, genome):
    from gtrackcore.core import Api
    filePath = os.path.join(dirname, filename)
    relFilePath = os.path.relpath(filePath)
    trackName = TRACK_NAME_SEP.join(os.path.normpath(relFilePath).split(os.sep))
    Api.importFile(filePath, genome, trackName)
    trackNameConverted = Api._convertTrackName(trackName)
    return PlainTrack(trackNameConverted)


def createSingleTrackTSFromFile(dirname, filename, genome, metadata={}):
    track = createTrackFromFile(dirname, filename, genome)
    if "title" not in metadata:
        metadata["title"] = os.path.join(dirname, filename)
    sts = SingleTrackTS(track, metadata)
    return sts

def createTrackStructureFromFileList(dirname, filenames, genome):
    ts = TrackStructureV2()
    for filename in filenames:
        ts[filename] = createSingleTrackTSFromFile(dirname, filename, genome)


def createTrackStructureFromFolder(inputFolderPath, genome):
    ts = TrackStructureV2()
    _updateTrackStructureFromFolder(ts, inputFolderPath, genome)
    return ts


def _updateTrackStructureFromFolder(ts, folderpath, genome):
    for directory, dirnames, filenames in os.walk(folderpath):
        if filenames:
            ts.update(createTrackStructureFromFileList(directory, filenames, genome))
        if dirnames:
            for dirname in dirnames:
                ts[dirname] = TrackStructureV2()
                _updateTrackStructureFromFolder(ts[dirname], dirname, genome)
        break

def createRandTrackStructure(origTS, tvProvider, randIndex):
    return origTS._getRandomizedVersion(tvProvider, randIndex)


