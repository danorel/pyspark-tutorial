### Prerequisites

1. python
2. java
3. scala (optional)
4. pyspark
5. netcat

### 1. Starting socket server using TCP protocol

```shell
nc -l 65432
```

To pass data to PySpark streaming service, type something to the **console**:

```shell
Hello, world
I need this power!
Good!
Well
hi
```

### 2. Starting PySpark streaming service

```shell
python3 main.py
```


PySpark reads and processes the data from socket server and prints it to **console**:
```
-------------------------------------------
Batch: 1
-------------------------------------------
+------------------+
|             value|
+------------------+
|      Hello, world|
|I need this power!|
|             Good!|
|              Well|
|                hi|
+------------------+
```