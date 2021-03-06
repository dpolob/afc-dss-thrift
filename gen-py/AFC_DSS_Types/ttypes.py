#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import AFC_Types.ttypes
import AFC_Sensors.ttypes

from thrift.transport import TTransport
all_structs = []


class AlgorithmStatus(object):
    Available = 0
    NotAvailable = 1
    Busy = 2

    _VALUES_TO_NAMES = {
        0: "Available",
        1: "NotAvailable",
        2: "Busy",
    }

    _NAMES_TO_VALUES = {
        "Available": 0,
        "NotAvailable": 1,
        "Busy": 2,
    }


class DssAlgorithm(object):
    """
    Attributes:
     - Id
     - Name
     - Description
     - Status
     - WebInterfaceUrl

    """


    def __init__(self, Id=None, Name=None, Description=None, Status=None, WebInterfaceUrl=None,):
        self.Id = Id
        self.Name = Name
        self.Description = Description
        self.Status = Status
        self.WebInterfaceUrl = WebInterfaceUrl

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.Id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.Name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.Description = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.Status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.WebInterfaceUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('DssAlgorithm')
        if self.Id is not None:
            oprot.writeFieldBegin('Id', TType.I32, 1)
            oprot.writeI32(self.Id)
            oprot.writeFieldEnd()
        if self.Name is not None:
            oprot.writeFieldBegin('Name', TType.STRING, 2)
            oprot.writeString(self.Name.encode('utf-8') if sys.version_info[0] == 2 else self.Name)
            oprot.writeFieldEnd()
        if self.Description is not None:
            oprot.writeFieldBegin('Description', TType.STRING, 3)
            oprot.writeString(self.Description.encode('utf-8') if sys.version_info[0] == 2 else self.Description)
            oprot.writeFieldEnd()
        if self.Status is not None:
            oprot.writeFieldBegin('Status', TType.I32, 4)
            oprot.writeI32(self.Status)
            oprot.writeFieldEnd()
        if self.WebInterfaceUrl is not None:
            oprot.writeFieldBegin('WebInterfaceUrl', TType.STRING, 5)
            oprot.writeString(self.WebInterfaceUrl.encode('utf-8') if sys.version_info[0] == 2 else self.WebInterfaceUrl)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ResponseNumber(object):
    """
    Attributes:
     - Timestamp
     - Observation
     - Units
     - Result

    """


    def __init__(self, Timestamp=None, Observation=None, Units=None, Result=None,):
        self.Timestamp = Timestamp
        self.Observation = Observation
        self.Units = Units
        self.Result = Result

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.Timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.Observation = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.Units = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.DOUBLE:
                    self.Result = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ResponseNumber')
        if self.Timestamp is not None:
            oprot.writeFieldBegin('Timestamp', TType.I64, 1)
            oprot.writeI64(self.Timestamp)
            oprot.writeFieldEnd()
        if self.Observation is not None:
            oprot.writeFieldBegin('Observation', TType.I32, 2)
            oprot.writeI32(self.Observation)
            oprot.writeFieldEnd()
        if self.Units is not None:
            oprot.writeFieldBegin('Units', TType.STRING, 3)
            oprot.writeString(self.Units.encode('utf-8') if sys.version_info[0] == 2 else self.Units)
            oprot.writeFieldEnd()
        if self.Result is not None:
            oprot.writeFieldBegin('Result', TType.DOUBLE, 4)
            oprot.writeDouble(self.Result)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ResponseBoolean(object):
    """
    Attributes:
     - Timestamp
     - Observation
     - Units
     - Result

    """


    def __init__(self, Timestamp=None, Observation=None, Units=None, Result=None,):
        self.Timestamp = Timestamp
        self.Observation = Observation
        self.Units = Units
        self.Result = Result

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.Timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.Observation = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.Units = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.Result = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ResponseBoolean')
        if self.Timestamp is not None:
            oprot.writeFieldBegin('Timestamp', TType.I64, 1)
            oprot.writeI64(self.Timestamp)
            oprot.writeFieldEnd()
        if self.Observation is not None:
            oprot.writeFieldBegin('Observation', TType.I32, 2)
            oprot.writeI32(self.Observation)
            oprot.writeFieldEnd()
        if self.Units is not None:
            oprot.writeFieldBegin('Units', TType.STRING, 3)
            oprot.writeString(self.Units.encode('utf-8') if sys.version_info[0] == 2 else self.Units)
            oprot.writeFieldEnd()
        if self.Result is not None:
            oprot.writeFieldBegin('Result', TType.BOOL, 4)
            oprot.writeBool(self.Result)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ResponseString(object):
    """
    Attributes:
     - Timestamp
     - Observation
     - Units
     - Result

    """


    def __init__(self, Timestamp=None, Observation=None, Units=None, Result=None,):
        self.Timestamp = Timestamp
        self.Observation = Observation
        self.Units = Units
        self.Result = Result

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.Timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.Observation = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.Units = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.Result = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ResponseString')
        if self.Timestamp is not None:
            oprot.writeFieldBegin('Timestamp', TType.I64, 1)
            oprot.writeI64(self.Timestamp)
            oprot.writeFieldEnd()
        if self.Observation is not None:
            oprot.writeFieldBegin('Observation', TType.I32, 2)
            oprot.writeI32(self.Observation)
            oprot.writeFieldEnd()
        if self.Units is not None:
            oprot.writeFieldBegin('Units', TType.STRING, 3)
            oprot.writeString(self.Units.encode('utf-8') if sys.version_info[0] == 2 else self.Units)
            oprot.writeFieldEnd()
        if self.Result is not None:
            oprot.writeFieldBegin('Result', TType.STRING, 4)
            oprot.writeString(self.Result.encode('utf-8') if sys.version_info[0] == 2 else self.Result)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ResponsePosition(object):
    """
    Attributes:
     - Timestamp
     - Observation
     - Units
     - Result

    """


    def __init__(self, Timestamp=None, Observation=None, Units=None, Result=None,):
        self.Timestamp = Timestamp
        self.Observation = Observation
        self.Units = Units
        self.Result = Result

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.Timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.Observation = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.Units = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.Result = AFC_Types.ttypes.Position()
                    self.Result.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ResponsePosition')
        if self.Timestamp is not None:
            oprot.writeFieldBegin('Timestamp', TType.I64, 1)
            oprot.writeI64(self.Timestamp)
            oprot.writeFieldEnd()
        if self.Observation is not None:
            oprot.writeFieldBegin('Observation', TType.I32, 2)
            oprot.writeI32(self.Observation)
            oprot.writeFieldEnd()
        if self.Units is not None:
            oprot.writeFieldBegin('Units', TType.STRING, 3)
            oprot.writeString(self.Units.encode('utf-8') if sys.version_info[0] == 2 else self.Units)
            oprot.writeFieldEnd()
        if self.Result is not None:
            oprot.writeFieldBegin('Result', TType.STRUCT, 4)
            self.Result.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(DssAlgorithm)
DssAlgorithm.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'Id', None, None, ),  # 1
    (2, TType.STRING, 'Name', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'Description', 'UTF8', None, ),  # 3
    (4, TType.I32, 'Status', None, None, ),  # 4
    (5, TType.STRING, 'WebInterfaceUrl', 'UTF8', None, ),  # 5
)
all_structs.append(ResponseNumber)
ResponseNumber.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'Timestamp', None, None, ),  # 1
    (2, TType.I32, 'Observation', None, None, ),  # 2
    (3, TType.STRING, 'Units', 'UTF8', None, ),  # 3
    (4, TType.DOUBLE, 'Result', None, None, ),  # 4
)
all_structs.append(ResponseBoolean)
ResponseBoolean.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'Timestamp', None, None, ),  # 1
    (2, TType.I32, 'Observation', None, None, ),  # 2
    (3, TType.STRING, 'Units', 'UTF8', None, ),  # 3
    (4, TType.BOOL, 'Result', None, None, ),  # 4
)
all_structs.append(ResponseString)
ResponseString.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'Timestamp', None, None, ),  # 1
    (2, TType.I32, 'Observation', None, None, ),  # 2
    (3, TType.STRING, 'Units', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'Result', 'UTF8', None, ),  # 4
)
all_structs.append(ResponsePosition)
ResponsePosition.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'Timestamp', None, None, ),  # 1
    (2, TType.I32, 'Observation', None, None, ),  # 2
    (3, TType.STRING, 'Units', 'UTF8', None, ),  # 3
    (4, TType.STRUCT, 'Result', [AFC_Types.ttypes.Position, None], None, ),  # 4
)
fix_spec(all_structs)
del all_structs
