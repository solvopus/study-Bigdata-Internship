# 1. 환경설치

## 1-1. 준비물

[MySQL 설치](https://dev.mysql.com/downloads/installer/)

<br>

MySQL Installer가 설치되면 Server와 Workbench를 반드시 설치하기

Workbench는 명령어를 입력하여 실행하는 커맨드라인(CLI)가 아닌, 사용자의 편의성을 높인 GUI 소프트웨어임

<br>

## 1-2. MySQL 실행

우측 아래의 트레이에 돌고래 모양을 우클릭한 뒤 MySQL80을 Running 상태로 만든다.

<br>

## 1-3. Workbench vs MySQL 8.0 Command Line Client

사용은 Workbench가 압도적으료 편하지만 문서상 이미지 첨부가 까다롭기에 CLI Client 기준으로 진행

<br><br>

# 2. Database 조작

SQL은 소문자나 대문자나 크게 상관은 없으나 대개 대문자를 사용

다만 일반적으론 프로젝트마다 설정된 규칙(convention)을 따름

## 2-1. Database 살펴보기

```mysql
SHOW DATABASES;
```

```MySQL
# 질의어에 대한 결과값
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| test               |
| world              |
+--------------------+
```

<br>

## 2-2. Database 생성 및 삭제

`CREATE DATABASE 데이터베이스명;`

`DROP DATABASE 데이터베이스명;`

<br>

```MYSQL
#생성
CREATE DATABASE practice;

Query OK, 1 row affected (0.01 sec)

#삭제
DROP DATABASE test;

SHOW DATABASES;
#결과값
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| practice           |
| sakila             |
| sys                |
| world              |
+--------------------+
```

<br>

## 2-3. Database 선택 (USE)

`USE 데이터베이스명;`

<br>

```MYS
USE practice;

#결과값
Database changed
```

<br>

<br>

# 3. Table 조작

## 3-1. Table 생성  (CREATE)

```MYSQL
CREATE TABLE 테이블명(
	필드명 타입,
    필드명 타입,
    필드명 타입,
    PRIMARY KEY(필드명)
);
```

<br>

```MYSQL
#테이블의 상위 범위인 데이터베이스를 USE 먼저 해야 함
SHOW DATABASES; #데이터베이스 목록 확인
USE practice; #practice라는 데이터베이스 선택

CREATE TABLE student(
	studentNumber VARCHAR(20),
    name VARCHAR(10),
    midExam int,
    finalExam int,
    address VARCHAR(30),
    PRIMARY KEY(studentNumber)
);
```

외래키나 기타 다른 설정도 가능하지만 가장 기초적인 질의어는 위와 같다

<br>

## 3-2. Table 확인하기 (DESC)

`DESC 질의어를 사용 (describe의 약어)`

`DESC 테이블명`

<br>

```MYSQL
SHOW TABLES;
#결과값
+--------------------+
| Tables_in_practice |
+--------------------+
| student            |
+--------------------+

DESC student;
#결과값
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| studentNumber | varchar(20) | NO   | PRI | NULL    |       |
| name          | varchar(10) | YES  |     | NULL    |       |
| midExam       | int         | YES  |     | NULL    |       |
| finalExam     | int         | YES  |     | NULL    |       |
| address       | varchar(30) | YES  |     | NULL    |       |
+---------------+-------------+------+-----+---------+-------+
```

<br>

## 3-3. Table 값 넣기  (INSERT INTO)

`INSERT INTO 명령어를 사용`

`INSERT INTO 테이블명 (필드명1, 필드명2, 필드명3, ...) VALUES (필드값1, 필드값2, 필드값3, ...)`

`INSERT INTO 테이블명 VALUES (필드값1, 필드값2, 필드값3, ...)`

```MYSQL
INSERT INTO student (studentNumber, name, midExam, finalExam, address)
VALUES ('1A8B3EF', '홍길동', 80, 70, '부산시 해운대구');

#해당 테이블 전체값 출력
SELECT * FROM student;
+---------------+--------+---------+-----------+-----------------+
| studentNumber | name   | midExam | finalExam | address         |
+---------------+--------+---------+-----------+-----------------+
| 1A8B3EF       | 홍길동 |      80 |        70 | 부산시 해운대구 |
+---------------+--------+---------+-----------+-----------------+
```

```MYSQL
#또 다른 표기법 - student 뒤 필드명은 생략이 가능 (실수할 가능성이 있기에 권장하진 않음)
INSERT INTO student VALUES ('2C8D5GA', '김하늘', 90, 55, '부산시 사상구');

#또 다른 표기법 - 굳이 넣고 싶지 않은 필드명은 생략이 가능하다
INSERT INTO student (studentNumber, name) VALUES ('8I9Z1DD', '기파랑');

#해당 테이블 전체값 출력
SELECT * FROM student;

+---------------+--------+---------+-----------+-----------------+
| studentNumber | name   | midExam | finalExam | address         |
+---------------+--------+---------+-----------+-----------------+
| 1A8B3EF       | 홍길동 |      80 |        70 | 부산시 해운대구 |
| 2C8D5GA       | 김하늘 |      90 |        55 | 부산시 사상구   |
| 8I9Z1DD       | 기파랑 |    NULL |      NULL | NULL            |
+---------------+--------+---------+-----------+-----------------+


```

<br>

## 3-4. Table 값 보기 (SELECT)

`SELECT 필드명 FROM 테이블명 WHERE 조건;`

```MYSQL
#에스터리스크(*)는 전부를 뜻함 => student 테이블에서 모든 필드명을 선택해서 봄
SELECT * FROM student; 

SELECT studentNumber, name FROM student;
+---------------+--------+
| studentNumber | name   |
+---------------+--------+
| 1A8B3EF       | 홍길동 |
| 2C8D5GA       | 김하늘 |
| 8I9Z1DD       | 기파랑 |
+---------------+--------+

SELECT studentNumber, name, address FROM student WHERE midExam >= 50;
+---------------+--------+-----------------+
| studentNumber | name   | address         |
+---------------+--------+-----------------+
| 1A8B3EF       | 홍길동 | 부산시 해운대구 |
| 2C8D5GA       | 김하늘 | 부산시 사상구   |
+---------------+--------+-----------------+

SELECT name, midExam, finalExam FROM student WHERE name = '홍길동';
+--------+---------+-----------+
| name   | midExam | finalExam |
+--------+---------+-----------+
| 홍길동 |      80 |        70 |
+--------+---------+-----------+
```

<br>

## 3-5. Table 값 수정 (UPDATE)

`UPDATE 테이블명 SET 필드1 = 데이터, 필드2 = 데이터, ..., WHERE 조건;`

<br>

```MYSQL
UPDATE student SET midExam = 50 WHERE name = "홍길동";
SELECT name, midExam, finalExam FROM student WHERE name = '홍길동';
+--------+---------+-----------+
| name   | midExam | finalExam |
+--------+---------+-----------+
| 홍길동 |      50 |        70 |
+--------+---------+-----------+
```

<br>

## 3-6. Table 값 삭제 (DELETE)

`DELETE FROM 테이블명 WHERE 조건;`

<br>

``` MYSQL
DELETE FROM student WHERE name = '기파랑';

+---------------+--------+---------+-----------+-----------------+
| studentNumber | name   | midExam | finalExam | address         |
+---------------+--------+---------+-----------+-----------------+
| 1A8B3EF       | 홍길동 |      50 |        70 | 부산시 해운대구 |
| 2C8D5GA       | 김하늘 |      90 |        55 | 부산시 사상구   |
+---------------+--------+---------+-----------+-----------------+
```

 

