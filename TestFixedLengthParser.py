import unittest as u
import FixedLengthParser as flp

class TestParse(u.TestCase):

    def setUp(self):
        self.fields = (
            flp.Field('one', 0, 10),
            flp.Field('two', 10, 5),
            flp.Field('three', 15, 30)
        )
        self.names = ('one', 'two', 'three')
        self.line = '{0[0]:<10}{0[1]:>5}{0[2]:^30}'.format([f.name for f in self.fields])
        self.calls = { 'two': lambda s: s[::-1] }
        
    def test_fields(self):
        with self.assertRaises(TypeError):
            flp.FixedLengthParser()
        
        p = flp.FixedLengthParser(self.fields)
        
        self.assertEqual(self.fields, p.fielddefs)
        self.assertEqual(self.names, p.fieldnames)
        
    def test_callbacks(self):
        p = flp.FixedLengthParser(self.fields, self.calls)
        
        self.assertEqual(self.calls, p.callbacks)
        self.assertEqual('tset', p.callbacks['two']('test'))
        
    def test_getfield(self):
        p = flp.FixedLengthParser(self.fields, self.calls)
        
        self.assertEqual('one', p.getField('one', self.line))
        self.assertEqual('owt', p.getField('two', self.line))
        self.assertEqual('three', p.getField('three', self.line))
        
    def test_getfields(self):
        p = flp.FixedLengthParser(self.fields, self.calls)
        
        fields = p.getFields(self.line)
        self.assertIsNotNone(fields)
        
        self.assertIn('one', fields)
        self.assertIn('two', fields)
        self.assertIn('three', fields)
        
        self.assertEqual('one', fields['one'])
        self.assertEqual('owt', fields['two'])
        self.assertEqual('three', fields['three'])

if __name__ == '__main__':
    u.main()