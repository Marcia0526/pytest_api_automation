import pytest
import allure


@allure.epic('计算器')
@allure.feature('乘与除')
class TestDivMulti:
    @allure.story('乘法运算')
    @allure.title('11*{num}')
    @allure.description('11的倍数')
    @pytest.mark.parametrize("num, output_value", [(1, 11), (2, 22), (3, 35), (4, 44)])
    def test_multiplication_11(self, num, output_value):
        assert 11 * num == output_value

    @allure.story('除法运算')
    @allure.title('{input_value}/13')
    @allure.description('13的余数')
    @pytest.mark.parametrize("input_value", [1, 13, 26, 39, 52])
    def test_divisible(self, input_value):
        assert input_value % 13 == 0
