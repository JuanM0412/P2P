# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: peer.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'peer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\npeer.proto\x12\x04peer\"+\n\x0fRegisterRequest\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\"\x1e\n\x10RegisterResponse\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1f\n\x11UnregisterRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"%\n\x12UnregisterResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\"\n\x14InternalTableRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"6\n\x15InternalTableResponse\x12\x1d\n\x05nodes\x18\x01 \x03(\x0b\x32\x0e.peer.NodeInfo\"0\n\x08NodeInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\t2\x9e\x02\n\x0bPeerService\x12\x39\n\x08Register\x12\x15.peer.RegisterRequest\x1a\x16.peer.RegisterResponse\x12?\n\nUnregister\x12\x17.peer.UnregisterRequest\x1a\x18.peer.UnregisterResponse\x12K\n\x10GetInternalTable\x12\x1a.peer.InternalTableRequest\x1a\x1b.peer.InternalTableResponse\x12\x46\n\x0bGetInterval\x12\x1a.peer.InternalTableRequest\x1a\x1b.peer.InternalTableResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'peer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGISTERREQUEST']._serialized_start=20
  _globals['_REGISTERREQUEST']._serialized_end=63
  _globals['_REGISTERRESPONSE']._serialized_start=65
  _globals['_REGISTERRESPONSE']._serialized_end=95
  _globals['_UNREGISTERREQUEST']._serialized_start=97
  _globals['_UNREGISTERREQUEST']._serialized_end=128
  _globals['_UNREGISTERRESPONSE']._serialized_start=130
  _globals['_UNREGISTERRESPONSE']._serialized_end=167
  _globals['_INTERNALTABLEREQUEST']._serialized_start=169
  _globals['_INTERNALTABLEREQUEST']._serialized_end=203
  _globals['_INTERNALTABLERESPONSE']._serialized_start=205
  _globals['_INTERNALTABLERESPONSE']._serialized_end=259
  _globals['_NODEINFO']._serialized_start=261
  _globals['_NODEINFO']._serialized_end=309
  _globals['_PEERSERVICE']._serialized_start=312
  _globals['_PEERSERVICE']._serialized_end=598
# @@protoc_insertion_point(module_scope)
