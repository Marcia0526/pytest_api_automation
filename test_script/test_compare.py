import pytest
import allure

@allure.epic('计算器')
@allure.feature('比较大小')
class TestCompare:
    @allure.story('大于')
    @allure.title('某个数大于100')
    @allure.description('比较某个数和100的大小关系')
    @pytest.mark.group_1
    def test_greater(self):
        num = 100
        assert num > 100

    @allure.story('大于等于')
    @allure.title('某个数大于等于100')
    @allure.description('比较某个数和100的关系')
    def test_greater_equal(self):
        num = 100
        assert num >= 100

    @allure.story('小于')
    @allure.title('某个数小于100')
    @allure.description('比较某个数和100的关系')
    @pytest.mark.group_1
    def test_less(self):
        num = 100
        assert num < 200



