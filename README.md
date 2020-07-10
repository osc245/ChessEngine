# ChessEngine
I did this to learn how to do OOP in python. This is my first python project so please forgive any javaisms that have bled into my python programming. The program includes a parser that converts chess notation into rows and columns and also has a few dozen unit tests. To run the program paste moves (one or many) in the console and the program will either show the board after those moves have been completed or print the first invalid move entered.

Chess notation:
Write moves in long algebraic notation. 
To move bishop from a1 to b2: Ba1-b2
To capture a queen on b2: Ba1xQb2
To capture a bishop en passen: a2xBb3ep
To promote to queen: a7-a8=Q
If move delivers check write “+” at the end: O-O+

