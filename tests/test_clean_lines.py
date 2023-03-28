import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from main import clean_paragraphs

@pytest.mark.events
class TestClean:
    @pytest.mark.parametrize(['texts', 'expected_text'], 
                            [('Hello\n World', 'Hello World'),
                             ('Bye \n World', 'Bye  World'),
                             ('Masdas\n World', 'Masdas World')])
    def test_clean_paragraphs(self, texts, expected_text):
        texts = clean_paragraphs(texts)
        assert expected_text == texts