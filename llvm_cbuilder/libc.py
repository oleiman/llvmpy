from .builder import CExternal
import llvm.core as lc
from . import shortnames as types

class LibC(CExternal):
    printf = lc.Type.function(types.int, [types.char_p], True)
    open = lc.Type.function(types.int, [types.char_p, types.int], True)
    read = lc.Type.function(types.int64, [types.int, types.void_p, types.int])
    calloc = lc.Type.function(types.void_p, [types.int, types.int])
    # TODO a lot more to add

