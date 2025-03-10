
from core.config.base import *
from core.config.fuzzer import FuzzerProxy
from core.config.jsanlyzer import JsAnalyzerProxy
from core.config.scanner import *
from core.config.enumerator import *

class RockConfig(ScannerProxy, CrawlerProxy, JsAnalyzerProxy, FuzzerProxy):

    def __init__(self) -> None:
        self.__mode       = None
        self.__output     = None
        self.__enumerator = None
        self.__verbose    = None

    def SetMode(self, mode: RockMode):
        self.__mode = mode

    def GetMode(self):
        return self.__mode.GetMode()

    def SetOutputConfig(self, output: OutputConfig):
        self.__output = output

    def GetOutputConfig(self):
        return self.__output

    def SetEnumeratorConfig(self, enumerator: EnumeratorConfig):
        self.__enumerator = enumerator

    def GetEnumeratorConfig(self):
        return self.__enumerator

    def SetVerbosity(self, v: Verbosity):
        self.__verbose = v

    def GetVerbosity(self):
        return self.__verbose
