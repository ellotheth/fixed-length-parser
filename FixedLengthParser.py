import collections as c

Field = c.namedtuple('field', ['name', 'start', 'length'])

class FixedLengthParser(object):
    
    def __init__(self, fields, callbacks = {}):
        self.fielddefs = fields
        self.callbacks = callbacks
        
        self.fieldnames = tuple([f.name for f in fields])
        
    def _parseValue(self, fielddef, line):
        lastpos = fielddef.start + fielddef.length
        if len(line) < lastpos: return None
        
        val = line[fielddef.start:lastpos]
        
        if fielddef.name in self.callbacks:
            val = self.callbacks[fielddef.name](val)
            
        return val.strip()
        
    def getFields(self, line):
        fields = c.OrderedDict()
        
        for f in self.fielddefs:
            fields[f.name] = self._parseValue(f, line)
            
        return fields
        
    def getField(self, name, line):
        for f in self.fielddefs:
            if name == f.name:
                return self._parseValue(f, line)
        
        return None
