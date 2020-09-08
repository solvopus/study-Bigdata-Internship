



- [1. 변수](#1---)
  * [1-1. 변수 할당 <-](#1-1---------)
  * [1-2. 변수의 형 확인](#1-2---------)
  * [1-.3 변수의 형](#1-3------)
    + [1-3-1. Numeric](#1-3-1-numeric)
    + [1-3-2. Factor](#1-3-2-factor)
    + [1-3-3. 그 외](#1-3-3----)
  * [1-4. 형 변환](#1-4-----)
- [2. 데이터 프레임](#2--------)
  * [2-1. 선언](#2-1---)
  * [2-2. 열 이름(column name)  변경하기](#2-2------column-name-------)
    + [2-2-1. 열 이름 한 번에 변경하기](#2-2-1---------------)
    + [2-2-2. 개별 변경](#2-2-2------)
    + [2-2-3.  열 이름 찾아 바꾸기](#2-2-3-------------)
    + [2-2-4. rename() 함수](#2-2-4-rename-----)
- [3. 함수](#3---)
  * [3-1. 함수 선언](#3-1------)
  * [3-2. 함수의 사용 이유](#3-2----------)
- [4. 데이터 파악](#4-------)
  * [4-1. 전체적인 데이터 파악하기](#4-1--------------)
  * [4-2. 데이터 열 이름 뽑아오기](#4-2--------------)
    + [4-2-1. names() 이용](#4-2-1-names-----)
    + [4-2-2. str() 이용](#4-2-2-str-----)
  * [4-3. 데이터 프레임 가공 및 추출](#4-3----------------)
    + [4-3-1. 열 선택하기](#4-3-1-------)
    + [4-3-2. 조건 넣기](#4-3-2------)
    + [4-3-3. 파생변수 생성](#4-3-3--------)
- [5. dplyr](#5-dplyr)
  * [5-1. 함수 목록](#5-1------)
  * [5-2. 파이프  연산자 (%>%)](#5-2---------------)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# 1. 변수


## 1-1. 변수 할당 <-

다른 프로그래밍 언어와는 달리 R에서 변수의 할당은 <- (화살표)를 사용함

=도 사용이 가능하나 <-를 권장 (몇몇 특수한 상황에선 =와 <-는 다른 값을 가지게 됨)

```R	
a <- 4
var1 <- 8
c <- 9

a <- c(1, 2, 3, 4, 5)
a <- c(1:5)
a <- seq(1, 5)
```

[c()에 관한 내용링크](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/c)

<br>

## 1-2. 변수의 형 확인

변수의 형(Type) 혹은 클래스 확인은 무엇보다 중요함

오류를 더불어 값의 누락 등이 일어날 수 있어 디버깅이 쉽지 않음

이는 class() 함수를 이용해 확인이 가능

```R
> a <- 1
> b <- 4
> class(a)
[1] "numeric"
> c <- data.frame(1)
> class(c)
[1] "data.frame"
```

<br>

## 1-.3 변수의 형

### 1-3-1. Numeric

연속 변수(Continous Variable)는 연속적이고 크기를 의미하는 값으로 구성된 변수

숫자가 크기를 지니기 때문에 양적 변수(Quantitative Variable)라고도 함



### 1-3-2. Factor

범주 변수(Categorical Variable)는 값이 대상을 분류하는 의미를 지닌 변수

예를 들어 성별을 1,2 로 범주를 분류할 경우 이 1과 2는 크기를 의미하지 않으므로 산술연산은 불가능함

명목 변수(Nominal Variable)라고도 부름



### 1-3-3. 그 외

integer(정수형), complex(복소수), character, logical, Date 등이 존재

<br>

## 1-4. 형 변환

```R
#as 함수 사용
as.typename(variable)

as.numeric(var)
```

<br><br>

# 2. 데이터 프레임

데이터 프레임에서 추출은 데이터 파악에 기술.

## 2-1. 선언

```R
data.frame() 함수를 사용해 할당가능
b <- data.frame(c(90, 80, 60, 70), c(55, 60, 45, 50))

b1 <- c(90, 80, 60, 70)
b2 <- c(55, 60, 45, 50)
b <- data.frame(b1, b2)
```

<br>

## 2-2. 열 이름(column name)  변경하기

### 2-2-1. 열 이름 한 번에 변경하기

```R
b1 <- c(90, 80, 60, 70)
b2 <- c(55, 60, 45, 50)
b <- data.frame(b1, b2)

names(b) = c("국어성적", "수학성적")
b
  국어성적 수학성적
1       90       55
2       80       60
3       60       45
4       70       50
```
<br>


### 2-2-2. 개별 변경

```r
b1 <- c(90, 80, 60, 70)
b2 <- c(55, 60, 45, 50)
b <- data.frame(b1, b2)

names(b)[1] <- "한자성적"
```
<br>


### 2-2-3.  열 이름 찾아 바꾸기 

```R
b1 <- c(90, 80, 60, 70)
b2 <- c(55, 60, 45, 50)
b <- data.frame(b1, b2)

names(b)[names(b) == "b1"] = "국어성적"
```

[names() 함수 관련링크](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/names)
<br>


### 2-2-4. rename() 함수

rename() 함수는 여러 패키지에 존재하지만 각각 문법이 다름

[rename 관련 자료](https://rfriend.tistory.com/41)

<br><br>

# 3. 함수

함수는 여러 명령어를 묶어놓은 명령어 모음이라 할 수 있다.

함수는 반환 값(return value)을 가진다. 반환 값은 하나의 값을 가지는 것이 일반적이다.

그러므로 함수에 많은 기능을 넣기보단 잘개 쪼개서 최소 기능만을 하도록 만들고, 그 작은 함수들을 모은 함수를 만들어 Bottom-Up 구조로 만드는 것이 권장된다.



## 3-1. 함수 선언

```R
함수명 = function(parameter1, parameter2, ...) {
    code
}
```



```R
#a와 b에 2를 곱하고 그 결과값에 3을 더한다

a <- 4
b <- 6
result = a * 2 + b * 2 + 3

calc = function(value1, value2) {
    result = value1 * 2 + value2 * 2 + 3
    return(result)
}
```
<br>


## 3-2. 함수의 사용 이유

함수의 사용은 크게 2가지 이득이 있다.

1. 코드의 재사용이 용이해진다.
2. 코드의 가독성이 높아진다.

```R
#a와 b에 2를 곱하고 그 결과값에 3을 더한다
#여기에 c와 d, e와 f의 값도 처리해야 한다면?

c <- 1
d <- 3
result = c * 2 + d * 2 + 3

e <- 10
f <- 11
result = e * 2 + f * 2 + 3
```

```R
#함수 사용 시
calc = function(value1, value2) {
    result = value1 * 2 + value2 * 2 + 3
    return(result)
}

c <- 1
d <- 3
e <- 10
f <- 11
result = calc(c, d)
result = calc(e, f)

```

위처럼 같은 기능을 수행하는 명령어가 많으면 많아질수록 중복이 일어나게 되는데 함수를 사용하면 재사용이 용이해진다.

<br><br>

# 4. 데이터 파악

## 4-1. 전체적인 데이터 파악하기

| 함수      |          기능           |
| --------- | :---------------------: |
| head()    |   데이터 앞부분 출력    |
| tail()    |   데이터 뒷부분 출력    |
| View()    | 뷰어 창에서 데이터 확인 |
| dim()     |    데이터 차원 출력     |
| str()     |    데이터 속성 출력     |
| summary() |    요약 통계량 출력     |

```R
library(gapminder)

head(gapminder) #기본 값은 6줄 출력
head(gapminder, 10) #10줄 출력

tail(gapminder)
tail(gapminder, 10) #뒤에서 10줄 출력

View(gapminder) #DB의 View창과 개념이 비슷함
dim(gapminder) #차원, 몇 행 몇 열인지를 출력함
str(gapminder) #각 변수들의 형(type) 보여줌

summary(gapminder) #통계 요약
```

<br>

## 4-2. 데이터 열 이름 뽑아오기

데이터 프레임에서 해당하는 열은 $ 혹은 인덱스 넘버 [number] 를 통해 선택할 수 있다.

하지만 데이터에 어떤 열이 있는지 모를 때는 어떻게 해야할까?

### 4-2-1. names() 이용

```R
library(gapminder)

> names(gapminder)
[1] "country"   "continent" "year"      "lifeExp"   "pop"       "gdpPercap"
```

<br>

### 4-2-2. str() 이용

```R
> str(gapminder)
tibble [1,704 x 6] (S3: tbl_df/tbl/data.frame)
 $ country  : Factor w/ 142 levels "Afghanistan",..: 1 1 1 1 1 1 1 1 1 1 ...
 $ continent: Factor w/ 5 levels "Africa","Americas",..: 3 3 3 3 3 3 3 3 3 3 ...
 $ year     : int [1:1704] 1952 1957 1962 1967 1972 1977 1982 1987 1992 1997 ...
 $ lifeExp  : num [1:1704] 28.8 30.3 32 34 36.1 ...
 $ pop      : int [1:1704] 8425333 9240934 10267083 11537966 13079460 14880372 12881816 13867957 16317921 22227415 ...
 $ gdpPercap: num [1:1704] 779 821 853 836 740 ...
```

<br>

## 4-3. 데이터 프레임 가공 및 추출

R 및 파이썬의 데이터 가공은 큰 덩어리를 깎아나가는 이미지에 가까움

네모난 석고상을 조각하면 조각할수록 그 이미지가 뚜렷해지는 것처럼 큰 덩어리의 데이터를 여러 함수나 연산자 등으로 필요한 정보만 추출함

### 4-3-1. 열 선택하기

방법은 크게 2가지로 $와 인덱스 넘버를 이용.

```R
#gapminder에서 country 값을 알고 싶을 경우
library(gapminder)

## 1.
unique(gapminder$country)
#unique 함수는 중복값을 제거하는 함수

## 2.
unique(gapminder[1])

```

<br>

### 4-3-2. 조건 넣기

방법은 크게 2가지

subset을 쓰거나 인덱스에 조건식을 넣어 사용할 수 있다

다만 이건 내장함수의 얘기이며 dplyr 처럼 다른 패키지를 쓰면 더 다양한 방법으로 조건을 넣을 수 있다

```R	
# 1. 인덱스를 이용
# 반드시 끝에 쉼표(,) 를 넣어야 행을 리턴함
gapminder[gapminder$country == "Afghanistan", ]

# 2. subset 이용
subset(gapminder$country == "Afghanistan")
subset(gapminder, country == "Afghanistan")
```

[두 가지 방법 중 무엇을 택할 지에 대한 Stack Overflow 자료](https://stackoverflow.com/questions/9860090/why-is-better-than-subset)

<br>

```R
#실습 예제
#주어진 countryList에 담긴 국가들의 데이터를 gapminder에서 뽑으시오
countryList <- c("Afghanistan", "Bolivia", "Burundi", "Canada", "Cuba", "Egypt", "France", "Germany", "Iceland")

```

```R
# 간략정답
result <- NULL

for (country in countryList) {
    verifyRow <- gapminder[gapminder$country == country, ]
	result <- rbind(result, verifyRow)
}

View(result)
```

<br>

### 4-3-3. 파생변수 생성

특정 연산 등을 통해 데이터 프레임에 새로운 변수를 생성할 수 있는데 이를 파생변수라고 한다.

```R
student_name = c("김하늘", "정바다", "이철수", "김전원", "정호언")
korean_midexam = c(55, 60, 85, 40, 67)
math_midexam = c(80, 88, 55, 65, 90)
eng_midexam = c(70, 72, 65, 88, 86)

studentsData = data.frame(student_name, korean_midexam, math_midexam, eng_midexam)
names(studentsData) = c("이름", "국어중간서적", "수학중간성적", "영어중간성적")

studentsData$평균 = (studentsData[2] + studentsData[3] + studentsData[4]) / 3

```

<br>

<br>

# 5. dplyr

dplyr은 여러 기능이 있는 패키지이나 주요 기능은 데이터 검색을 SQL처럼 사용할 수 있게 만드는 기능임

dplyr을 제대로 쓰려면 최소한의 SQL 쿼리에 대한 지식이 필요



## 5-1. 함수 목록

| 함수        | 기능              |
| ----------- | ----------------- |
| filter()    | 행 추출           |
| select()    | 열(변수) 추출     |
| arrange()   | 정렬              |
| mutate()    | 변수 추가         |
| summarise() | 통계치 산출       |
| group_by    | 집단별로 나누기   |
| left_join() | 데이터 합치기(열) |
| bind_rows() | 데이터 합치기(행) |

<br>

## 5-2. 파이프  연산자 (%>%)

파이프 연산자의 단축키는 Ctrl + Shift + M 

파이프 연산자는 왼쪽에서 오른쪽으로 읽을 수 있도록 만드는 연산자이다

보통의 함수는 y = h(e(f(g(x)))) 이처럼 안에서 밖으로 읽어나가지만 파이프 연산자를 이용하면 밖에서 안으로 순차적으로 연산이 가능하다

<br>

```R
x <- c(1, 2, 3, 4, 5)
x <- 1:5 %<% c()
```

[관련 추가 자료](https://gomguard.tistory.com/243)

<br>

## 5-3. filter()

해당하는 데이터의 행을 추출한다

```R
library(gapminder)
library(dplyr)

filter(gapminder, country == "France")

# 파이프 연산자 사용 시
gapminder %>% filter(country == "France")
```



## 5-4. select()

해당하는 데이터의 열을 추출한다

SQL의 쿼리를 다룬 경험이 있다면 매우 익숙한 함수

SQL과의 차이점은 WHERE 문으로 조건을 붙이는 SQL 쿼리와는 달리 조건은 다른 함수를 쓰고, select는 해당 데이터의 열만을 출력할 때 종종 쓰인다

```R
library(gapminder)
library(dplyr)

select(gapminder, country)

#파이프 연산자 사용 시
gapminder %>% select(country)


```



## 5-5. group_by

집단별로 나누는 함수로 SQL의 group과 사용용도는 비슷하다

