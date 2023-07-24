from gendiff.constants import ADDED, CHANGED, UNCHANGED, NESTED, REMOVED
from gendiff.parser import parse
from gendiff.gen_diff import gendiff


before_dict = parse("./tests/fixtures/before.json")
after_dict = parse("./tests/fixtures/after.json")


def test_gendiff():
    result = gendiff(before_dict, after_dict)

    assert result == {
        "common": (NESTED, {
            "setting1": (UNCHANGED, "Value 1"),
            "setting2": (REMOVED, "200"),
            "setting3": (UNCHANGED, True),
            "setting4": (ADDED, "blah blah"),
            "setting5": (ADDED, {"key5": "value5"}),
            "setting6": (REMOVED, {"key": "value"})
        }),
        "group1": (NESTED, {
            "baz": (CHANGED, "bas", "bars"),
            "foo": (UNCHANGED, "bar")
        }),
        "group2": (REMOVED, {"abc": "12345"}),
        "group3": (ADDED, {"fee": "100500"})
    }