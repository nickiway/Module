import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from main import compare_sentences

@pytest.mark.events
class TestCompare:
    @pytest.mark.parametrize(['f1_info', 'f2_info', 'expected'], 
                            [(["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                            "Fusce eu commodo arcu. Phasellus imperdiet convallis turpis."],
                            ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                            "Phasellus imperdiet convallis turpis.",
                            "Fusce eu commodo arcu."], 
                            [{"Lorem ipsum dolor sit amet, consectetur adipiscing elit."}, 
                            {"Fusce eu commodo arcu. Phasellus imperdiet convallis turpis.", 
                            "Phasellus imperdiet convallis turpis.",
                            "Fusce eu commodo arcu."}])])
    
    def test_compare_files(self, f1_info, f2_info, expected):
        assert compare_sentences(f1_info, f2_info) == expected