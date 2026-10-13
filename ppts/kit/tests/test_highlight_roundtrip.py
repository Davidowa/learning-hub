import unittest

from kit.highlight import highlight


class HighlightRoundTrip(unittest.TestCase):
    def test_native_numeric_literals_keep_every_character(self):
        source = 'var speed = 10f; var t = 0.7f; var n = 1e5; var mask = 0x1F;'
        for language in ('csharp', 'cpp', 'swift', 'typescript'):
            with self.subTest(language=language):
                spans = highlight(source, language)
                self.assertEqual(source, ''.join(text for text, _ in spans[0]))
                numbers = [text for text, role in spans[0] if role == 'num']
                self.assertEqual(['10f', '0.7f', '1e5', '0x1F'], numbers)

    def test_unknown_identifiers_and_unicode_are_preserved(self):
        source = 'var café = 1_000UL; var odd = 123abc; // café\n'
        spans = highlight(source, 'csharp')
        self.assertEqual(source.rstrip('\n'), '\n'.join(''.join(text for text, _ in row) for row in spans))


if __name__ == '__main__':
    unittest.main()
