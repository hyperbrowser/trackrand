from trackrand.utils.TrackStructureUtils import createTrackStructureFromFolder, createRandTrackStructure, \
    createSingleTrackTSFromFile


def _resolveTvProviderClsFromRandAlgorithm(randAlgorithm, allowOverlaps):
    pass


def _getBinSourceForGenome(genome):
    pass


def getTvProviderFromRandAlg(origßTS, randAlgorithm, genome, allowOverlaps, excludedTs=None, **kwargs):
    tvProviderCls = _resolveTvProviderClsFromRandAlgorithm(randAlgorithm)
    binSource = _getBinSourceForGenome(genome)
    return tvProviderCls(origTS, binSource=binSource, excludedTs=excludedTs, allowOverlaps=allowOverlaps)


class RandomizationRunner(object):

    @classmethod
    def run(cls, inputFolderPath, outputFolderPath, genome, randAlgorithm, excludedPath=None, allowOverlaps=False, nrSamples=1, **kwargs):
        origTS = createTrackStructureFromFolder(inputFolderPath, genome)
        excludedTs = cls._createExcludedTrackStructureFromPath(excludedPath)
        tvProvider = getTvProviderFromRandAlg(origTS, randAlgorithm, genome, allowOverlaps, excludedTs=excludedTs, **kwargs)
        for i in xrange(nrSamples):
            randTS = createRandTrackStructure(origTS, tvProvider, i)
            cls._writeTrackStructure(randTS, outputFolderPath, i)


    @classmethod
    def _writeTrackStructure(cls, trackStructure, outputFolderPath, i):
        pass

    @classmethod
    def _createExcludedTrackStructureFromPath(cls, excludedPath, genome):
        if excludedPath is None:
            return None
        import os
        if os.path.isdir(excludedPath):
            return createTrackStructureFromFolder(excludedPath, genome)
        else: #is single file
            return createSingleTrackTSFromFile("", excludedPath, genome)

