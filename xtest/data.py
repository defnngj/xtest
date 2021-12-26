import csv
import json
import warnings
import codecs
from itertools import islice
from functools import wraps
from parameterized.parameterized import inspect
from parameterized.parameterized import parameterized
from parameterized.parameterized import default_doc_func
from parameterized.parameterized import default_name_func
from parameterized.parameterized import skip_on_empty_helper
from parameterized.parameterized import reapply_patches_if_need
from parameterized.parameterized import delete_patches_if_need
from parameterized import parameterized_class


def file_data(file=None, line=0):
    """
    数据文件参数化
    :param file:
    :return:
    """
    if file is None:
        raise FileNotFoundError("请指定数据文件")
    file_type = file.split(".")[-1]
    if file_type == "json":
        with open(file, 'r') as load_f:
            load_dict = json.load(load_f)
        return data(load_dict)
    elif file_type == "csv":
        csv_obj = csv.reader(codecs.open(file, 'r', 'utf_8_sig'))
        data_list = []
        for line in islice(csv_obj, line, None):
            data_list.append(line)
        return data(data_list)
    else:
        raise TypeError("文件类型不支持")


def data(input, name_func=None, doc_func=None, skip_on_empty=False, **legacy):
    """ A "brute force" method of parameterizing test cases. Creates new
        test cases and injects them into the namespace that the wrapped
        function is being defined in. Useful for parameterizing tests in
        subclasses of 'UnitTest', where Nose test generators don't work.
        >> @data([("foo", 1, 2)])
        ... def test_add1(name, input, expected):
        ...     actual = add1(input)
        ...     assert_equal(actual, expected)
        ...
        >> locals()
        ... 'test_add1_foo_0': <function ...> ...
        >>
        """

    if "testcase_func_name" in legacy:
        warnings.warn("testcase_func_name= is deprecated; use name_func=",
                      DeprecationWarning, stacklevel=2)
        if not name_func:
            name_func = legacy["testcase_func_name"]

    if "testcase_func_doc" in legacy:
        warnings.warn("testcase_func_doc= is deprecated; use doc_func=",
                      DeprecationWarning, stacklevel=2)
        if not doc_func:
            doc_func = legacy["testcase_func_doc"]

    doc_func = doc_func or default_doc_func
    name_func = name_func or default_name_func

    def parameterized_expand_wrapper(f, instance=None):
        frame_locals = inspect.currentframe().f_back.f_locals

        parameters = parameterized.input_as_callable(input)()

        if not parameters:
            if not skip_on_empty:
                raise ValueError(
                    "Parameters iterable is empty (hint: use "
                    "`parameterized.expand([], skip_on_empty=True)` to skip "
                    "this test when the input is empty)"
                )
            return wraps(f)(skip_on_empty_helper)

        digits = len(str(len(parameters) - 1))
        for num, p in enumerate(parameters):
            name = name_func(f, "{num:0>{digits}}".format(digits=digits, num=num), p)
            # If the original function has patches applied by 'mock.patch',
            # re-construct all patches on the just former decoration layer
            # of param_as_standalone_func so as not to share
            # patch objects between new functions
            nf = reapply_patches_if_need(f)
            frame_locals[name] = parameterized.param_as_standalone_func(p, nf, name)
            frame_locals[name].__doc__ = doc_func(f, num, p)

        # Delete original patches to prevent new function from evaluating
        # original patching object as well as re-constructed patches.
        delete_patches_if_need(f)

        f.__test__ = False

    return parameterized_expand_wrapper


def date_class(attrs, input_values):
    """
    参数化类
    :param attrs: 
    :param input_values: 
    :return: 
    """""
    return parameterized_class(attrs, input_values)


























