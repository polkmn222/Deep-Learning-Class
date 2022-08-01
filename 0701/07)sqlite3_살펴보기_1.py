# -*- coding: utf-8 -*-
"""07)sqlite3-살펴보기-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MgCVcIgJcpZwCVWoyoP8JF_NFWDCrn0b

### ***sqlite3와 Jupyter Notebook의 python과의 연결을 위해서는 미리 sqlite3를 설치하시길 바랍니다***

"sqlite3 라이브러리"의 버전과 "SQLite(DB 엔진)"버전을 출력해보자
"""

import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

# DB 생성 (오토 커밋)
# isolation_level= None이라고 하는 것은 쿼리문을 실행하여
# DB에 즉시 반영, 즉시 자동 커밋(commit)을 해보기 위함이다.

conn = sqlite3.connect("test.db", isolation_level = None)

# 커서 획득
c = conn.cursor()

# 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
c.execute("CREATE TABLE IF NOT EXISTS table1 \
(id integet PRIMARY KEY, name text, birthday text)")

"""### 데이터 삽입하기"""

# 데이터 삽입 방법 1
c.execute("INSERT INTO table1 \
    VALUES(1,'PARK','2022-00-00')")

# 데이터 삽입 방법 2
c.execute("INSERT INTO table1(id, name, birthday)\
    VALUES(?,?,?)",\
         (2,'KIM','2021-00-00'))

test_tuple = (
    (3,'LEE', '2020-00-00'),
    (4,'CHOI', '2019-00-00'),
    (5,'JUNG', '2018-00-00')
)

c.executemany("INSERT INTO table1(id, name, birthday) VALUES(?,?,?)", test_tuple)

"""### 데이터 불러오기"""

c.execute("SELECT * FROM table1")

print(c.fetchone()) # c.fetchone()을 사용하면 한 줄씩 출력하는 걸 확인가능하다
print(c.fetchone()) # 단, 이미 출력한 이후의 자료들만 차례대로 출력이 된다.
print(c.fetchall()) # c.fetchall()함수를 활용하여 전체를 출력한다.
                    # 다만, 이미 읽었던 지점 이후부터 전체가 출력된다.

"""만약 전체 데이터를 출력하고 싶다면 아래와 같이 전체를 다시 실행 후 다시 진행해야 한다"""

c.execute("SELECT * FROM table1")
print(c.fetchall())

"""위의 데이터는 리스트로 출력되는 것을 확인가능한데, 결국 이는 for문을 적용할 수 있음을 의미한다."""

# 방법 1
c.execute("SELECT * FROM table1")
for row in c.fetchall():
    print(row)

# 방법 2
for row in c.execute("SELECT * FROM table1"):
    print(row)

"""### 데이터 조회하기 (필터링)

SQL에서 WHERE문을 써야 합니다.
"""

# 방법 1
param1 = (1,)
c.execute('SELECT * FROM table1 WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())

# 방법 2
param2 = 1
c.execute("SELECT * FROM table1 WHERE id='%s'" % param2) # %s %d %f
print('param2', c.fetchone())
print('param2', c.fetchall())

# 방법 3
c.execute("SELECT * FROM table1 WHERE id=ID", {"Id":1}) # %s %d %f
print('param3', c.fetchone())
print('param3', c.fetchall())

# 방법 4
param4 = (1,4)
c.execute("SELECT * FROM table1 WHERE id IN(?,?)", param4) 
print('param4', c.fetchall())

# 방법 5
c.execute("SELECT * FROM table1 WHERE id IN('%d','%d')" % (1,4)) 
print('param6', c.fetchall())

# 방법 6
c.execute("SELECT * FROM table1 WHERE id=:id1 OR id=:id2", {"id1":1, "id2":4})
print('param6', c.fetchall())

"""### 데이터 수정하기"""

# 방법1
c.execute("UPDATE table1 SET name=? WHERE id=?", ('NEW1', 1))

# 방법2
c.execute("UPDATE table1 SET name=:name WHERE id=:id", {"name":'NEW2', 'id':3})

# 방법2
c.execute("UPDATE table1 SET name='%s' WHERE id='%s'" % ('NEW3', 5))

# 수정된 데이터 확인
for row in c.execute('SELECT * FROM table1'):
    print(row)

"""### 데이터 삭제하기"""

# 방법 1
c.execute("DELETE FROM table1 WHERE id=?", (1,))

# 방법 2
c.execute("DELETE FROM table1 WHERE id=:id", {'id':3})

# 방법 3
c.execute("DELETE FROM table1 WHERE id='%s'" % 5)

# 확인
for row in c.execute('SELECT * FROM table1'):
    print(row)

### 모든 테이블의 데이터 전체를 지우려면 conn.execute()안에 쿼리문을 써주면 된다.

# 방법1
# conn.execute("DELETE FROM table1")

# 방법1
print(conn.execute("DELETE FROM table1").rowcount) # rowcount property는 지운 행의 개수를 보여줌

"""2,4의 데이터 2개만 있었을 때에 2개를 지웠으므로 2라는 숫자가 나왔다.

### sqlite3 - 연결해제

DB를 연결해서 CRUD를 수행하였다면 마지막엔 그 연결을 해제하여야 한다. 그래서 항상 conn.close()로 마무리를 한다.

### DB 백업하기 (dump)

DB는 항상 dump를 통해 백업을 해놓는게 중요하다.
"""

with conn:
    with open('dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Completed.')

"""위의 코드를 수행하고 sql파일을 열어보면 아래의 형태와 같이 호출된다."""

BEGIN TRANSACTION;
CREATE TABLE table1(id integer PRIMARY KEY, name text, birthday text);
INSERT INTO "table1" VALUES(1,'LEE','1987-00-00');
INSERT INTO "table1" VALUES(2,'KIM','1990-00-00');
INSERT INTO "table1" VALUES(3,'PARK','1991-00-00');
INSERT INTO "table1" VALUES(4,'CHOI','1999-00-00');
INSERT INTO "table1" VALUES(5,'JUNG','1989-00-00');
COMMIT;

# end of files