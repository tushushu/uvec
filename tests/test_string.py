from typing import List, Union

import pytest
import ulist as ul
from ulist.utils import check_test_result

LIST_TYPE = Union[List[float], List[int], List[bool], List[str]]


@pytest.mark.parametrize(
    "test_method, nums, expected_value, kwargs",
    [
        (
            "contains",
            ["num1", "num2", "element1", "element2"],
            [True, True, False, False],
            {"elem": "num"},
        ),
    ],
)
def test_methods_with_args(
    test_method: str,
    nums: List[str],
    expected_value: List[str],
    kwargs: dict,
) -> None:
    dtype = "string"
    arr = ul.from_seq(nums, dtype=dtype)
    result = getattr(arr, test_method)(**kwargs)
    check_test_result(dtype, test_method, result, expected_value)