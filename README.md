0x00. Pascal's Triangle

Algorithm

Python

 By: Alexa Orrico, Software Engineer at Holberton School

 Weight: 1

 Ongoing second chance project - started Apr 17, 2023 6:00 AM, must end by Apr 24, 2023 6:00 AM

 An auto review will be launched at the deadline

review: 11.0/11 mandatory

Altogether:  100.0%

Mandatory: 100.0%



Concepts

For this project, we expect you to look at this concept:

Technical interview

Tasks

0. Pascal's Triangle

mandatory



Returns an empty list if n <= 0

You can assume n will be always an integer

guillaume@ubuntu:~/0x00$ cat 0-main.py

#!/usr/bin/python3

"""

0-main

"""

pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):

    """

    Print the triangle

    """

    for row in triangle:

        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":

    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 

guillaume@ubuntu:~/0x00$ ./0-main.py

[1]

[1,1]

[1,2,1]

[1,3,3,1]

[1,4,6,4,1]

guillaume@ubuntu:~/0x00$ 

Repo:

GitHub repository: alx-interview

Directory: 0x00-pascal_triangle

File: 0-pascal_triangle.py
