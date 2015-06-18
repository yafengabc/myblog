title: 在C++中使用GMP（二）：为什么要用C++
date: 2015-06-18 20:09:09
tags:
- linux
- c++
- C++
- gmp
categories: C++
---
##在C++中使用gmp（二）：为什么要用C++##

上一篇中，写了一个小小的例子，用gmp库写了个100的阶乘，文中我提到，网上的例子多为C风格，  
我却倾向于用C++风格，C++风格有什么好处呢？我们看以下代码：
```C
#include <stdio.h>
#include <gmp.h>

int main()
{
    mpz_t res;
    res=1;
    int i=1;
    for (i=1;i!=100;++i)
    {
        res*=i;
    }
    printf("%s",res);
    return 0;
}

```
我把代码写成了C风格，代码看起来没什么问题，但是实际编译却出现了问题：
```bash
gcc test.c -lgmp
test.c: In function ‘main’:
test.c:7:8: error: assignment to expression with array type
res=1;
^
test.c:11:12: error: assignment to expression with array type
res*=i;
^
```
原来，大数的类型mpz_t不是基本类型，是无法直接用=号赋值的，需要用函数
来完成，经过一番改动，最终等效结果如下：
```C
#include <stdio.h>
#include <gmp.h>

int main()
{
    mpz_t res;
    mpz_init(res);
    mpz_set_ui(res,1);
    int i=1;
    for (i=1;i!=100;++i)
    {
        mpz_mul_ui(res,res,i);
    }
    gmp_printf("%Zd",res);
    return 0;
}
```
- 所有的赋值，必须用函数，四则运算也必须用函数；
- 使用前，要用init函数初始化；
- 标准的输入输出函数不能用，要用专用的gmp_开头的函数。














---
Writed by Yafeng
