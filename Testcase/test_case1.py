#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/18 17:33
# @Author  : wangjun
# @File    : case1.py
# @explain : pytest练习训练

import pytest


def sub(a, b):
    c = a - b
    return c


def f():
    return 4


def test_sub():
    assert sub(10, 8) == 6, '计算结果不正确'


def test_f():
    assert f() == 3, '函数返回值是不为3'


# 参数化测试功能：@pytest.mark.parametrize
@pytest.mark.parametrize('test_input, expected', [('1+1', 2), ('4*6', 24), ('5*5', '30')])
def test_eval(test_input,expected):
    assert eval(test_input) == expected, '结果计算错误！'


@pytest.mark.parametrize('x', [0, 2])
@pytest.mark.parametrize('y', [8, 6])
def test_add(x, y):
    """
    分别对应（0，8）（0，6） （2,8） （2,6）
    """
    assert x == y



if __name__ == '__main__':
    pytest.main(['a'])
