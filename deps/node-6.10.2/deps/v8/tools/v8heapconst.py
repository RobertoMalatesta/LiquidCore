# Copyright 2013 the V8 project authors. All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#     * Neither the name of Google Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# This file is automatically generated from the V8 source and should not
# be modified manually, run 'make grokdump' instead to update this file.

# List of known V8 instance types.
INSTANCE_TYPES = {
  64: "STRING_TYPE",
  68: "ONE_BYTE_STRING_TYPE",
  65: "CONS_STRING_TYPE",
  69: "CONS_ONE_BYTE_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  71: "SLICED_ONE_BYTE_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  70: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  82: "SHORT_EXTERNAL_STRING_TYPE",
  86: "SHORT_EXTERNAL_ONE_BYTE_STRING_TYPE",
  90: "SHORT_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  0: "INTERNALIZED_STRING_TYPE",
  4: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  6: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  18: "SHORT_EXTERNAL_INTERNALIZED_STRING_TYPE",
  22: "SHORT_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  26: "SHORT_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  130: "SIMD128_VALUE_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  131: "ODDBALL_TYPE",
  171: "CELL_TYPE",
  174: "PROPERTY_CELL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  149: "FILLER_TYPE",
  150: "ACCESSOR_INFO_TYPE",
  151: "ACCESSOR_PAIR_TYPE",
  152: "ACCESS_CHECK_INFO_TYPE",
  153: "INTERCEPTOR_INFO_TYPE",
  154: "CALL_HANDLER_INFO_TYPE",
  155: "FUNCTION_TEMPLATE_INFO_TYPE",
  156: "OBJECT_TEMPLATE_INFO_TYPE",
  157: "SIGNATURE_INFO_TYPE",
  158: "TYPE_SWITCH_INFO_TYPE",
  160: "ALLOCATION_MEMENTO_TYPE",
  159: "ALLOCATION_SITE_TYPE",
  161: "SCRIPT_TYPE",
  162: "CODE_CACHE_TYPE",
  163: "POLYMORPHIC_CODE_CACHE_TYPE",
  164: "TYPE_FEEDBACK_INFO_TYPE",
  165: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  166: "BOX_TYPE",
  175: "PROTOTYPE_INFO_TYPE",
  176: "SLOPPY_BLOCK_WITH_EVAL_CONTEXT_EXTENSION_TYPE",
  169: "FIXED_ARRAY_TYPE",
  148: "FIXED_DOUBLE_ARRAY_TYPE",
  170: "SHARED_FUNCTION_INFO_TYPE",
  172: "WEAK_CELL_TYPE",
  173: "TRANSITION_ARRAY_TYPE",
  179: "JS_MESSAGE_OBJECT_TYPE",
  178: "JS_VALUE_TYPE",
  180: "JS_DATE_TYPE",
  181: "JS_OBJECT_TYPE",
  182: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  183: "JS_GENERATOR_OBJECT_TYPE",
  184: "JS_MODULE_TYPE",
  185: "JS_GLOBAL_OBJECT_TYPE",
  186: "JS_GLOBAL_PROXY_TYPE",
  187: "JS_ARRAY_TYPE",
  188: "JS_ARRAY_BUFFER_TYPE",
  189: "JS_TYPED_ARRAY_TYPE",
  190: "JS_DATA_VIEW_TYPE",
  177: "JS_PROXY_TYPE",
  191: "JS_SET_TYPE",
  192: "JS_MAP_TYPE",
  193: "JS_SET_ITERATOR_TYPE",
  194: "JS_MAP_ITERATOR_TYPE",
  195: "JS_ITERATOR_RESULT_TYPE",
  196: "JS_WEAK_MAP_TYPE",
  197: "JS_WEAK_SET_TYPE",
  198: "JS_PROMISE_TYPE",
  199: "JS_REGEXP_TYPE",
  200: "JS_BOUND_FUNCTION_TYPE",
  201: "JS_FUNCTION_TYPE",
  167: "DEBUG_INFO_TYPE",
  168: "BREAK_POINT_INFO_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  0x08081: (136, "ByteArrayMap"),
  0x080ad: (132, "MetaMap"),
  0x080d9: (131, "NullMap"),
  0x08105: (169, "FixedArrayMap"),
  0x08131: (4, "OneByteInternalizedStringMap"),
  0x0815d: (138, "FreeSpaceMap"),
  0x08189: (149, "OnePointerFillerMap"),
  0x081b5: (149, "TwoPointerFillerMap"),
  0x081e1: (131, "UndefinedMap"),
  0x0820d: (129, "HeapNumberMap"),
  0x08239: (131, "TheHoleMap"),
  0x08265: (131, "BooleanMap"),
  0x08291: (131, "UninitializedMap"),
  0x082bd: (171, "CellMap"),
  0x082e9: (174, "GlobalPropertyCellMap"),
  0x08315: (170, "SharedFunctionInfoMap"),
  0x08341: (134, "MutableHeapNumberMap"),
  0x0836d: (130, "Float32x4Map"),
  0x08399: (130, "Int32x4Map"),
  0x083c5: (130, "Uint32x4Map"),
  0x083f1: (130, "Bool32x4Map"),
  0x0841d: (130, "Int16x8Map"),
  0x08449: (130, "Uint16x8Map"),
  0x08475: (130, "Bool16x8Map"),
  0x084a1: (130, "Int8x16Map"),
  0x084cd: (130, "Uint8x16Map"),
  0x084f9: (130, "Bool8x16Map"),
  0x08525: (169, "NativeContextMap"),
  0x08551: (133, "CodeMap"),
  0x0857d: (169, "ScopeInfoMap"),
  0x085a9: (169, "FixedCOWArrayMap"),
  0x085d5: (148, "FixedDoubleArrayMap"),
  0x08601: (172, "WeakCellMap"),
  0x0862d: (173, "TransitionArrayMap"),
  0x08659: (68, "OneByteStringMap"),
  0x08685: (169, "FunctionContextMap"),
  0x086b1: (131, "NoInterceptorResultSentinelMap"),
  0x086dd: (131, "ArgumentsMarkerMap"),
  0x08709: (131, "ExceptionMap"),
  0x08735: (131, "TerminationExceptionMap"),
  0x08761: (169, "HashTableMap"),
  0x0878d: (169, "OrderedHashTableMap"),
  0x087b9: (128, "SymbolMap"),
  0x087e5: (64, "StringMap"),
  0x08811: (69, "ConsOneByteStringMap"),
  0x0883d: (65, "ConsStringMap"),
  0x08869: (67, "SlicedStringMap"),
  0x08895: (71, "SlicedOneByteStringMap"),
  0x088c1: (66, "ExternalStringMap"),
  0x088ed: (74, "ExternalStringWithOneByteDataMap"),
  0x08919: (70, "ExternalOneByteStringMap"),
  0x08945: (70, "NativeSourceStringMap"),
  0x08971: (82, "ShortExternalStringMap"),
  0x0899d: (90, "ShortExternalStringWithOneByteDataMap"),
  0x089c9: (0, "InternalizedStringMap"),
  0x089f5: (2, "ExternalInternalizedStringMap"),
  0x08a21: (10, "ExternalInternalizedStringWithOneByteDataMap"),
  0x08a4d: (6, "ExternalOneByteInternalizedStringMap"),
  0x08a79: (18, "ShortExternalInternalizedStringMap"),
  0x08aa5: (26, "ShortExternalInternalizedStringWithOneByteDataMap"),
  0x08ad1: (22, "ShortExternalOneByteInternalizedStringMap"),
  0x08afd: (86, "ShortExternalOneByteStringMap"),
  0x08b29: (140, "FixedUint8ArrayMap"),
  0x08b55: (139, "FixedInt8ArrayMap"),
  0x08b81: (142, "FixedUint16ArrayMap"),
  0x08bad: (141, "FixedInt16ArrayMap"),
  0x08bd9: (144, "FixedUint32ArrayMap"),
  0x08c05: (143, "FixedInt32ArrayMap"),
  0x08c31: (145, "FixedFloat32ArrayMap"),
  0x08c5d: (146, "FixedFloat64ArrayMap"),
  0x08c89: (147, "FixedUint8ClampedArrayMap"),
  0x08cb5: (169, "SloppyArgumentsElementsMap"),
  0x08ce1: (169, "CatchContextMap"),
  0x08d0d: (169, "WithContextMap"),
  0x08d39: (169, "BlockContextMap"),
  0x08d65: (169, "ModuleContextMap"),
  0x08d91: (169, "ScriptContextMap"),
  0x08dbd: (169, "ScriptContextTableMap"),
  0x08de9: (179, "JSMessageObjectMap"),
  0x08e15: (135, "ForeignMap"),
  0x08e41: (181, "NeanderMap"),
  0x08e6d: (181, "ExternalMap"),
  0x08e99: (160, "AllocationMementoMap"),
  0x08ec5: (159, "AllocationSiteMap"),
  0x08ef1: (163, "PolymorphicCodeCacheMap"),
  0x08f1d: (161, "ScriptMap"),
  0x08f75: (137, "BytecodeArrayMap"),
  0x08fa1: (166, "BoxMap"),
  0x08fcd: (150, "AccessorInfoMap"),
  0x08ff9: (151, "AccessorPairMap"),
  0x09025: (152, "AccessCheckInfoMap"),
  0x09051: (153, "InterceptorInfoMap"),
  0x0907d: (154, "CallHandlerInfoMap"),
  0x090a9: (155, "FunctionTemplateInfoMap"),
  0x090d5: (156, "ObjectTemplateInfoMap"),
  0x09101: (162, "CodeCacheMap"),
  0x0912d: (164, "TypeFeedbackInfoMap"),
  0x09159: (165, "AliasedArgumentsEntryMap"),
  0x09185: (167, "DebugInfoMap"),
  0x091b1: (168, "BreakPointInfoMap"),
  0x091dd: (175, "PrototypeInfoMap"),
  0x09209: (176, "SloppyBlockWithEvalContextExtensionMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("OLD_SPACE", 0x08081): "NullValue",
  ("OLD_SPACE", 0x08095): "EmptyDescriptorArray",
  ("OLD_SPACE", 0x0809d): "EmptyFixedArray",
  ("OLD_SPACE", 0x080c9): "UndefinedValue",
  ("OLD_SPACE", 0x080f5): "NanValue",
  ("OLD_SPACE", 0x08105): "TheHoleValue",
  ("OLD_SPACE", 0x08129): "TrueValue",
  ("OLD_SPACE", 0x08161): "FalseValue",
  ("OLD_SPACE", 0x08189): "empty_string",
  ("OLD_SPACE", 0x08195): "hidden_string",
  ("OLD_SPACE", 0x081a1): "UninitializedValue",
  ("OLD_SPACE", 0x081d1): "EmptyByteArray",
  ("OLD_SPACE", 0x081d9): "NoInterceptorResultSentinel",
  ("OLD_SPACE", 0x08219): "ArgumentsMarker",
  ("OLD_SPACE", 0x08249): "Exception",
  ("OLD_SPACE", 0x08275): "TerminationException",
  ("OLD_SPACE", 0x082ad): "NumberStringCache",
  ("OLD_SPACE", 0x08ab5): "SingleCharacterStringCache",
  ("OLD_SPACE", 0x08f4d): "StringSplitCache",
  ("OLD_SPACE", 0x09355): "RegExpMultipleCache",
  ("OLD_SPACE", 0x0975d): "EmptyFixedUint8Array",
  ("OLD_SPACE", 0x0976d): "EmptyFixedInt8Array",
  ("OLD_SPACE", 0x0977d): "EmptyFixedUint16Array",
  ("OLD_SPACE", 0x0978d): "EmptyFixedInt16Array",
  ("OLD_SPACE", 0x0979d): "EmptyFixedUint32Array",
  ("OLD_SPACE", 0x097ad): "EmptyFixedInt32Array",
  ("OLD_SPACE", 0x097bd): "EmptyFixedFloat32Array",
  ("OLD_SPACE", 0x097cd): "EmptyFixedFloat64Array",
  ("OLD_SPACE", 0x097dd): "EmptyFixedUint8ClampedArray",
  ("OLD_SPACE", 0x097ed): "InfinityValue",
  ("OLD_SPACE", 0x097fd): "MinusZeroValue",
  ("OLD_SPACE", 0x0980d): "MinusInfinityValue",
  ("OLD_SPACE", 0x0981d): "MessageListeners",
  ("OLD_SPACE", 0x09839): "CodeStubs",
  ("OLD_SPACE", 0x0feb9): "DummyVector",
  ("OLD_SPACE", 0x13fed): "NonMonomorphicCache",
  ("OLD_SPACE", 0x14601): "PolymorphicCodeCache",
  ("OLD_SPACE", 0x14609): "NativesSourceCache",
  ("OLD_SPACE", 0x1488d): "ExperimentalNativesSourceCache",
  ("OLD_SPACE", 0x148c1): "ExtraNativesSourceCache",
  ("OLD_SPACE", 0x148e1): "ExperimentalExtraNativesSourceCache",
  ("OLD_SPACE", 0x148ed): "EmptyScript",
  ("OLD_SPACE", 0x1492d): "IntrinsicFunctionNames",
  ("OLD_SPACE", 0x2e919): "EmptyPropertiesDictionary",
  ("OLD_SPACE", 0x2e965): "UndefinedCell",
  ("OLD_SPACE", 0x2e96d): "ObservationState",
  ("OLD_SPACE", 0x2e979): "ScriptList",
  ("OLD_SPACE", 0x2eb01): "ClearedOptimizedCodeMap",
  ("OLD_SPACE", 0x2eb0d): "EmptyWeakCell",
  ("OLD_SPACE", 0x534d1): "EmptySlowElementDictionary",
  ("OLD_SPACE", 0x5351d): "WeakObjectToCodeTable",
  ("OLD_SPACE", 0x53631): "ArrayProtector",
  ("OLD_SPACE", 0x53641): "EmptyPropertyCell",
  ("OLD_SPACE", 0x53651): "NoScriptSharedFunctionInfos",
  ("OLD_SPACE", 0x59cf1): "StringTable",
  ("CODE_SPACE", 0x1a001): "JsEntryCode",
  ("CODE_SPACE", 0x1e721): "JsConstructEntryCode",
}