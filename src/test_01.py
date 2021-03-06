# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 06:40
# @Author  : hexiangxuan
# @File    : test_case.py
import allure
import pytest
from locallib.add_tags import add_tag


@allure.epic('自动化用例')
@allure.feature('大模块')
@allure.story('小模块')
@pytest.mark.auto
class TestOne:
    def setup_class(self):
        pass

    @allure.title("获取标签数据信息")
    @allure.severity("critical")
    @pytest.mark.critical
    def test_case_01(self):
        """
        author：xiangxuan
        describe: 获取标签数据信息
        """
        add_tag('网购达人')
        assert 0 == 0

    @allure.title("新增标签")
    @allure.severity("normal")
    @pytest.mark.normal
    @allure.issue('https://www.baidu.com', '百度首页')
    def test_case_02(self):
        """
        作者：xiangxuan
        描述：新增一个标签
        """
        assert 0 == 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
