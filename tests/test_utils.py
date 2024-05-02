import pytest
from great_tables._utils import (
    _assert_list_is_subset,
    _assert_str_in_set,
    _assert_str_list,
    _assert_str_scalar,
    _collapse_list_elements,
    _insert_into_list,
    _match_arg,
    _str_scalar_to_list,
    _unique_set,
    heading_has_subtitle,
    heading_has_title,
)


def test_heading_has_title():
    assert heading_has_title("title")
    assert not heading_has_title(None)


def test_heading_has_subtitle():
    assert heading_has_subtitle("subtitle")
    assert not heading_has_subtitle(None)


def test_match_arg():
    assert _match_arg("x", ["a", "b", "c", "x"]) == "x"


def test_match_arg_raises():
    with pytest.raises(ValueError) as exc_info:
        _match_arg("x", [])

    assert "The `lst` object must contain at least one element." in exc_info.value.args[0]

    with pytest.raises(ValueError) as exc_info:
        _match_arg("x", [1])

    assert "All elements in the `lst` object must be strings." in exc_info.value.args[0]

    with pytest.raises(ValueError) as exc_info:
        _match_arg("x", ["a", "a"])

    assert "The `lst` object must contain unique elements." in exc_info.value.args[0]

    with pytest.raises(ValueError) as exc_info:
        _match_arg("x", ["a"])

    assert "is not an allowed option." in exc_info.value.args[0]


def test_assert_str_scalar():
    _assert_str_scalar("a")


def test_assert_str_scalar_raises():
    with pytest.raises(AssertionError) as exc_info:
        _assert_str_scalar(1)

    assert "is not a string." in exc_info.value.args[0]


def test_assert_str_list():
    _assert_str_list(["a"])


def test_assert_str_list_raises():
    with pytest.raises(AssertionError) as exc_info:
        _assert_str_list(1)

    assert "is not a list." in exc_info.value.args[0]

    with pytest.raises(AssertionError) as exc_info:
        _assert_str_list([1])

    assert "Not all elements of the supplied list are strings." in exc_info.value.args[0]


def test_assert_str_in_set():
    _assert_str_in_set("a", ["a", "b", "c"])


def test_assert_str_in_set_raises():
    with pytest.raises(AssertionError) as exc_info:
        _assert_str_in_set("x", ["a", "b", "c"])

    assert "is not part of the defined `set`." in exc_info.value.args[0]


def test_assert_list_is_subset():
    _assert_list_is_subset([1, 2], [1, 2, 3])


def test_assert_list_is_subset_raises():
    with pytest.raises(AssertionError) as exc_info:
        _assert_list_is_subset([1, 2], [2, 3, 4])

    assert "The columns provided are not present in the table." in exc_info.value.args[0]


def test_str_scalar_to_list():
    x = _str_scalar_to_list("x")
    assert isinstance(x, list)
    assert x[0] == "x"


def test_unique_set_None():
    assert _unique_set(None) is None


def test_unique_set():
    x = ["a", "a", "b"]
    result = _unique_set(x)
    assert isinstance(result, list)
    assert len(result) == 2


def test_collapse_list_elements():
    lst = ["a", "b", "c"]
    assert _collapse_list_elements(lst) == "abc"
    assert _collapse_list_elements(lst, "#") == "a#b#c"


def test_insert_into_list():
    lst = ["b", "c"]
    assert _insert_into_list(lst, "a") == ["a", "b", "c"]
