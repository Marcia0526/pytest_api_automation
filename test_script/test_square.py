import math
import allure

@allure.epic('计算器')
@allure.feature('幂运算')
class TestSqrt:
    @allure.story('开方运算')
    @allure.title('25的开方')
    def test_sqrt(self):
        num = 25
        assert math.sqrt(num) == 5

    @allure.story('乘方运算')
    @allure.title('7的乘方')
    def testsquare(self):
        num = 7
        assert 7 * 7 == 40



