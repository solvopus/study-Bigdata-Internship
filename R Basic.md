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



# 2. 데이터 프레임

## 2-1. 선언

```R
data.frame() 함수를 사용해 할당가능
b <- data.frame(c(90, 80, 60, 70), c(55, 60, 45, 50))

b1 <- c(90, 80, 60, 70)
b2 <- c(55, 60, 45, 50)
b <- data.frame(b1, b2)
```



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



### 2-2-2. 개별 변경

```r
b1 <- c(90, 80, 60, 70)
b2 <- c(55, 60, 45, 50)
b <- data.frame(b1, b2)

names(b)[1] <- "한자성적"
```



### 2-2-3.  열 이름 찾아 바꾸기 

```R
b1 <- c(90, 80, 60, 70)
b2 <- c(55, 60, 45, 50)
b <- data.frame(b1, b2)

names(b)[names(b) == "b1"] = "국어성적"
```

[names() 함수 관련링크](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/names)



### 2-2-4. rename() 함수

rename() 함수는 여러 패키지에 존재하지만 각각 문법이 다름

[rename 관련 자료](https://rfriend.tistory.com/41)



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



# 4. 데이터 프레임

