# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import p2p_pb2 as p2p__pb2

GRPC_GENERATED_VERSION = '1.65.4'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in p2p_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class P2PServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.JoinNetwork = channel.unary_unary(
                '/p2p.P2PService/JoinNetwork',
                request_serializer=p2p__pb2.JoinRequest.SerializeToString,
                response_deserializer=p2p__pb2.JoinResponse.FromString,
                _registered_method=True)
        self.LeaveNetwork = channel.unary_unary(
                '/p2p.P2PService/LeaveNetwork',
                request_serializer=p2p__pb2.LeaveRequest.SerializeToString,
                response_deserializer=p2p__pb2.LeaveResponse.FromString,
                _registered_method=True)
        self.UploadFile = channel.unary_unary(
                '/p2p.P2PService/UploadFile',
                request_serializer=p2p__pb2.FileTransferRequest.SerializeToString,
                response_deserializer=p2p__pb2.FileTransferResponse.FromString,
                _registered_method=True)
        self.DownloadFile = channel.unary_unary(
                '/p2p.P2PService/DownloadFile',
                request_serializer=p2p__pb2.FileTransferRequest.SerializeToString,
                response_deserializer=p2p__pb2.FileTransferResponse.FromString,
                _registered_method=True)
        self.Ping = channel.unary_unary(
                '/p2p.P2PService/Ping',
                request_serializer=p2p__pb2.PingRequest.SerializeToString,
                response_deserializer=p2p__pb2.PingResponse.FromString,
                _registered_method=True)
        self.LookupID = channel.unary_unary(
                '/p2p.P2PService/LookupID',
                request_serializer=p2p__pb2.LookupRequest.SerializeToString,
                response_deserializer=p2p__pb2.LookupResponse.FromString,
                _registered_method=True)
        self.UpdateFTable = channel.unary_unary(
                '/p2p.P2PService/UpdateFTable',
                request_serializer=p2p__pb2.UpdateFTableRequest.SerializeToString,
                response_deserializer=p2p__pb2.UpdateFTableResponse.FromString,
                _registered_method=True)
        self.GetFingerTable = channel.unary_unary(
                '/p2p.P2PService/GetFingerTable',
                request_serializer=p2p__pb2.Empty.SerializeToString,
                response_deserializer=p2p__pb2.FingerTableResponse.FromString,
                _registered_method=True)


class P2PServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def JoinNetwork(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LeaveNetwork(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFingerTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_P2PServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'JoinNetwork': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinNetwork,
                    request_deserializer=p2p__pb2.JoinRequest.FromString,
                    response_serializer=p2p__pb2.JoinResponse.SerializeToString,
            ),
            'LeaveNetwork': grpc.unary_unary_rpc_method_handler(
                    servicer.LeaveNetwork,
                    request_deserializer=p2p__pb2.LeaveRequest.FromString,
                    response_serializer=p2p__pb2.LeaveResponse.SerializeToString,
            ),
            'UploadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=p2p__pb2.FileTransferRequest.FromString,
                    response_serializer=p2p__pb2.FileTransferResponse.SerializeToString,
            ),
            'DownloadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=p2p__pb2.FileTransferRequest.FromString,
                    response_serializer=p2p__pb2.FileTransferResponse.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=p2p__pb2.PingRequest.FromString,
                    response_serializer=p2p__pb2.PingResponse.SerializeToString,
            ),
            'LookupID': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupID,
                    request_deserializer=p2p__pb2.LookupRequest.FromString,
                    response_serializer=p2p__pb2.LookupResponse.SerializeToString,
            ),
            'UpdateFTable': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFTable,
                    request_deserializer=p2p__pb2.UpdateFTableRequest.FromString,
                    response_serializer=p2p__pb2.UpdateFTableResponse.SerializeToString,
            ),
            'GetFingerTable': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFingerTable,
                    request_deserializer=p2p__pb2.Empty.FromString,
                    response_serializer=p2p__pb2.FingerTableResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'p2p.P2PService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('p2p.P2PService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class P2PService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def JoinNetwork(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/p2p.P2PService/JoinNetwork',
            p2p__pb2.JoinRequest.SerializeToString,
            p2p__pb2.JoinResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LeaveNetwork(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/p2p.P2PService/LeaveNetwork',
            p2p__pb2.LeaveRequest.SerializeToString,
            p2p__pb2.LeaveResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UploadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/p2p.P2PService/UploadFile',
            p2p__pb2.FileTransferRequest.SerializeToString,
            p2p__pb2.FileTransferResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/p2p.P2PService/DownloadFile',
            p2p__pb2.FileTransferRequest.SerializeToString,
            p2p__pb2.FileTransferResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/p2p.P2PService/Ping',
            p2p__pb2.PingRequest.SerializeToString,
            p2p__pb2.PingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LookupID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/p2p.P2PService/LookupID',
            p2p__pb2.LookupRequest.SerializeToString,
            p2p__pb2.LookupResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateFTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/p2p.P2PService/UpdateFTable',
            p2p__pb2.UpdateFTableRequest.SerializeToString,
            p2p__pb2.UpdateFTableResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetFingerTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/p2p.P2PService/GetFingerTable',
            p2p__pb2.Empty.SerializeToString,
            p2p__pb2.FingerTableResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
