from gtrackcore.util.CustomExceptions import AbstractClassError

NUMBER_OF_SEGMENTS = 'Number of segments'
COVERAGE = 'Base pair coverage'

class TsBasedRandomTrackViewProvider(object):
    def __init__(self, origTs, binSource=None, excludedTs=None,  allowOverlaps=False, **kwargs):
        self._origTs = origTs
        self._allowOverlaps = allowOverlaps
        self._excludedTs = excludedTs
        self._binSource = binSource
        self._kwArgs = kwargs


    def getTrackView(self, region, origTrack, randIndex):
        raise AbstractClassError

class BetweenTrackRandomTvProvider(TsBasedRandomTrackViewProvider):
    def __init__(self, *args, **kwArgs):
        raise AbstractClassError

class WithinTrackRandomTvProvider(TsBasedRandomTrackViewProvider):
    def __init__(self, *args, **kwArgs):
        raise AbstractClassError

