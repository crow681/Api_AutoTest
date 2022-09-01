#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/19 10:10
# @Author  : wangjun
# @File    : test_case2.py
# @explain : pytest fixtures的使用(夹具)
"""
pytest fixtures相当于unittest中的setup/teardown函数，对测试进行初始化，函数参数通常在test之后命名为fixture
较setup和teardown的区别：
1.装置有明确名称，通过在测试函数、模块、类或项目中来声明激活；
2.夹具以模块化的方式实现，因为每个夹具名称触发夹具功能；
3.允许根据配置和组件选项参数化夹具和测试，或可跨功能、类、模块或在整个测试范围内重复使用
4.不需要在自定义卸载夹具清理
夹具使用pytest.fixtures装饰器
"""

import pytest


@pytest.fixture
def first_entry():
    return 'a'


@pytest.fixture
def order(first_entry):
    return []


@pytest.fixture(autouse=True)      # 自动执行，即使不使用被声明的函数，在执行测试也会被调用
def append_fisrt(order, first_entry):
    return order.append(first_entry)


def test_string(order, first_entry):
    order.append('b')
    assert order == [first_entry, 'b']


if __name__ == "__main__":
    pytest.main(['-ra'])