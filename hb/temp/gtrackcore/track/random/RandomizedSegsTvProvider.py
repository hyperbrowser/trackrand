from gtrackcore.track.random.PermutedSegsAndIntersegsTrack import PermutedSegsAndIntersegsTrack
from gtrackcore.track.random.PermutedSegsAndSampledIntersegsTrack import PermutedSegsAndSampledIntersegsTrack
from gtrackcore.util.CustomExceptions import NotSupportedError
from temp.gtrackcore.track.random.TsBasedRandomTrackViewProvider import WithinTrackRandomTvProvider, \
    TsBasedRandomTrackViewProvider


class PermutedSegsAndIntersegsTrackViewProvider(WithinTrackRandomTvProvider):
    def __init__(self, origTs, allowOverlaps=False, **kwargs):
        if allowOverlaps == True:
            raise NotSupportedError('Overlaps are not supported in this type of randomization')
        TsBasedRandomTrackViewProvider.__init__(self, origTs, allowOverlaps=allowOverlaps, **kwargs)

    def getTrackView(self, region, origTrack, randIndex):
        return PermutedSegsAndIntersegsTrack(origTrack, randIndex).getTrackView(region)

class PermutedSegsAndSampledIntersegsTrackViewProvider(WithinTrackRandomTvProvider):
    def __init__(self, origTs, allowOverlaps=False, **kwargs):
        if allowOverlaps == True:
            raise NotSupportedError('Overlaps are not supported in this type of randomization')
        TsBasedRandomTrackViewProvider.__init__(self, origTs, allowOverlaps=allowOverlaps, **kwargs)

    def getTrackView(self, region, origTrack, randIndex):
        return PermutedSegsAndSampledIntersegsTrack(origTrack, randIndex).getTrackView(region)

