# 2024 / 04 /09 / 화요일


# 서로 연관된 코드를 묶어서 파일로 저장한 후 이름을 붙이면 "모듈"이라고 함 
# 그 모듈을 또 정리정돈해서 묶어두면 "패키지"라고 함 
# 패키지를 또 정리정돈해두면 "객체(Object)"라고 함 

"""
    즉, list,dictionary + function = object(객체)
    object 정리한 게 "Module"
    이런 Module을 정리정돈한게 Pakage

"""


#==================================================

"""

        def sum(a,b):
            return a+b

        def sum(a,b):
            return 'average : ' + str((a+b)/2)  

        print(sum(1,2))   


    만약 위에 이름이 같은 두 함수가 있을 때 제일 마지막에 작성한 함수만 실행이 됨!
    내가 실행되길 원한 함수가 맨 위에 함수라면 심각한 문제가 발생!!

    --> 그래서 앞에 접두사를 따로 붙여주면 된다고 함 
    --> 예)  def arithmetic_sum(a,b):
             def statistics_sum(a,b):

    --> 이때 같은 이름을 가진 함수가 너무나 많다면 접두사 붙이기 귀찮고, 조금 지저분해보일 수 있음 
    --> 해결 방법은 "모듈"이라고 함




"""

# 모듈을 이용해서 각각 파일에다가 이름이 같은 함수를 작성하고 
# 여기에서 그 함수들을 가져와서 써보자 
# 방법은 import해주면 된다고 함 
# 작성법 : import 파일명(확장자는 쓰지 말기)

"""

// 패키지 수업을 위해서 구분해놓기
// 이건 arithmetic_module.py와 statistics_module.py이 
   entry.py랑 같은 패키지 안에 있을 경우
   (즉, number_pakage 패키지 안에 있지 않았을 경우)

import arithmetic_module
import statistics_module



# import해준 파일에 있는 함수를 이용해서 계산하고 싶다면?
# 모듈명.함수이름(num1,num2)

print(arithmetic_module.sum(2,2))   
print(statistics_module.sum(25,5)) 

===> 아주 실행이 잘 됨 


---------------------------------------------------------------

# 더 간편한 방법 
# from 모듈명 import 함수명

from statistics_module import sum

print(sum(1,2))

"""

# 만약 모듈에 저장되있는 함수를 여기에서 불러올 때 함수명을 변경하고 싶다면?
# 작성법 from 모듈명 import 함수명 as 변경할 함수명(혹은 별명)


"""

from statistics_module import sum as ssum

print(ssum(1,2))



    그런데 또 모듈이 너무 많아지면 정리정돈하고 싶어짐
    -> 디렉토리를 만들고, 그 디렉토리 안에 연관된 모듈을 넣고 적당한 이름을 붙이면 된다고 함 
    ===> 이게 바로 패키지

"""


# ====================== 패키지 수업 ===============================

"""
number_pakage 패키지 안에 arithmetic_module.py랑 statistics_module.py가 있음

""" 

# 1. 
# number_pakage 안에 모듈이 이동되어 있는데 statistics_module.py를 여기서 실행하고 싶다면?
# 모듈 import하는 법 : import 패키지 명.모듈명
# 출력시 : print(import 패키지명.모듈명.함수명(num1,num2))

"""
import number_pakage.statistics_module
print(number_pakage.statistics_module.sum(1,2))

---> 결과 제대로 출력됨

"""


# 2. from을 써서 출력해보자
# 작성법 from 물리적인 경로(패키지명.모듈명) import 함수명
# 출력시 print(함수명(num1,num2))

"""
from number_pakage.statistics_module import sum
print(sum(1,2))
--> 결과 제대로 출력됨

"""

# 3. 함수에 별명을 지정하고 싶다면?
# from 물리적인 경로(패키지명.모듈명) import 함수명 as 별명 
# 출력시 print(별명(num1,num2))

"""
from number_pakage.statistics_module import sum as newsum
print(newsum(2,4))
--> 제대로 출력됨

"""