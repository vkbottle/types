import pytest
from utils.strings_util import (
    categorize_methods_as_files, get_type_from_reference,
    snake_case_to_camel_case
)


@pytest.mark.parametrize(
    "test_input,expected",
    [('snake_case', 'SnakeCase'),
     ('testestestestest', 'Testestestestest'),
     ('estest.estest.est', 'Estest.estest.est'),
     (['snake_case', 'snake_case'], {'snake_case': 'SnakeCase'})
     ]
)
def test_snake_case(test_input, expected):
    assert snake_case_to_camel_case(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [('referef/efgegeg/sdg/another_reference', 'AnotherReference'),
     ('afgafasf/agdaga/AnotherReference', 'AnotherReference'),
     ('pathpathpathpathpath/ref.ref', 'Ref.ref')
     ]
)
def test_get_type_from_reference(test_input, expected):
    assert get_type_from_reference(test_input) == expected


def test_categorize_methods_as_files():
    test_json = {
        'methods': [{
                'name': 'account.ban'
            },
            {
                'name': 'account.changePassword'
            },
            {
                'name': 'account.getActiveOffers'
            },
            {
                'name': 'groups.getSettings'
            }
        ]
    }

    assert categorize_methods_as_files(
                                      test_json) == {'account': {},
                                                     'groups': {}}
