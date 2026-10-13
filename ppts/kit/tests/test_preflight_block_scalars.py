import tempfile
import unittest
from pathlib import Path
from kit.preflight import check

class BlockScalarTests(unittest.TestCase):
    def check_text(self, text):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'lesson.yaml';path.write_text(text)
            return check(str(path))[0]

    def test_typescript_properties_are_code_not_yaml_fields(self):
        text="""meta:
  lang: en
slides:
  - code:
      title: Typed callback
      source: |
        const options = {
          add: (id: string) => id,
          title: 'Report',
        };
"""
        self.assertEqual(self.check_text(text), [])

    def test_bad_scalar_after_code_is_still_reported(self):
        text="""meta:
  lang: en
slides:
  - code:
      source: |
        const options = { id: '1' };
      title: Example: callback
"""
        self.assertTrue(any('unquoted colon' in x for x in self.check_text(text)))

    def test_style_rule_still_applies_inside_code(self):
        text="""meta:
  lang: en
slides:
  - code:
      title: Example
      source: |
        // A—B
"""
        self.assertTrue(any('em dash' in x for x in self.check_text(text)))

if __name__=='__main__':unittest.main()
