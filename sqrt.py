import numpy as np
import math


def sqrt_dic(x, precision=1e-10):
    ''' 
       开根号
       利用二分法对一个正数开根号
       Args:
            x : 被开方数 
            precision : 精度默认值1e-10
       Return : 
            返回求出来的根（float）
    '''
    left, right = 0.0, float(x)
    if precision < 0:
        raise RuntimeError('precision 必须是一个大于0的值')
    if x < precision:
        raise RuntimeError('x 必须是一个大于精度{}的值'.format(precision))
    elif x < 1:
        right = 1

    middle = (right - left) / 2 + left
    while(middle * middle - x > precision or middle * middle - x < -precision):
        middle = (right - left) / 2 + left
        if(middle * middle > x):
            right = middle
        elif middle * middle < x:
            left = middle
    return middle


def sqrt_newton(x, precision=1e-10):
    '''
       开根号
       利用牛顿迭代法对一个正数开根号
        Args:
            x : 被开方数 
            precision : 精度默认值1e-10
        Return :
           返回求出来的根（float） 
        Errors
    '''
    res = x
    if x < 0:
        raise RuntimeError('x必须是一个正数')
    elif precision < 0:
        raise RuntimeError('precision必须是一个大于0的值')
    while(res * res - x > precision or res * res - x < -precision):
        res = (res + x/res) / 2

    return res


# 测试代码
# for i in np.arange(1, 100, 0.5):
#     error = math.fabs(math.sqrt(i)-sqrt_dic(i))
#     if error < 1e-10:
#         print('{} pass!!!'.format(i))
#     else:
#         print('{} fail!!! 误差为{} {}开平方的结果为{} '.format(i, error, i, sqrt_dic(i)))
# print(sqrt_dic(-1))

# print(sqrt_dic(0.0))

# print(sqrt_newton(0.5))
for i in np.arange(1, 100, 0.5):
    error = math.fabs(math.sqrt(i)-sqrt_newton(i))
    if error < 1e-10:
        print('{} pass!!!'.format(i))
    else:
        print('{} fail!!! 误差为{} {}开平方的结果为{} '.format(
            i, error, i, sqrt_newton(i)))
