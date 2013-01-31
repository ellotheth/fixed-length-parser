import collections as c

Field = c.namedtuple('field', ['name', 'start', 'length'])

class FixedLengthParser(object):
    """Helpers for basic parsing of fields in fixed-length text records"""
    
    def __init__(self, fields, callbacks = {}):
        """Define the parsing structure.
        
        fields
            An iterator of Field namedtuples (or really anything with the
            properties in Field) that define the record structure. Note that
            fields of zero length are allowed, if you want insert data not in
            the record.
        callbacks
            A dictionary of callbacks tied to field names that will transform
            or modify the raw field values.
            
        """
            
        self.fielddefs = fields
        self.callbacks = callbacks
        
        # not sure if this should be here. it's convenient, for now.
        self.fieldnames = tuple([f.name for f in fields])
        
    def _parseValue(self, fielddef, line):
        # pull a field value out of the text record
        
        # if the line is too short for this field, skip it
        lastpos = fielddef.start + fielddef.length
        if len(line) < lastpos: return None
        
        val = line[fielddef.start:lastpos]
        
        # run modifiers, if necessary
        if fielddef.name in self.callbacks:
            val = self.callbacks[fielddef.name](val)
            
        # always return null if the field is empty
        return val.strip() if len(val) else None
        
    def getFields(self, line):
        """Pull the raw text record into an ordered dictionary of fields"""
        fields = c.OrderedDict()
        
        for f in self.fielddefs:
            fields[f.name] = self._parseValue(f, line)
            
        return fields
        
    def getField(self, name, line):
        """Grab one field, by name, from a text record"""
        for f in self.fielddefs:
            if name == f.name:
                return self._parseValue(f, line)
        
        return None

    def parseFile(self, filename, skipConditions = ()):
        """Read a file and convert one line a a time to ordered dictionaries
        
        skipConditions
            An iterator of callbacks that return True or False. Each line of the
            file is run against each skip condition; if any return True, the
            line is skipped.
            
        """
        with open(filename, 'r') as f:
            for line in f:
                if True in [skip(line) for skip in skipConditions]: continue
                yield self.getFields(line)
