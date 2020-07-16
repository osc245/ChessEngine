# ChessProgram
I did this project to practice OOP in Python. This is my first Python project so please forgive any Javaisms that have bled into my Python programming. The program includes a parser that converts chess notation into rows and columns and also has a few dozen unit tests. To run the program paste moves (one or many) in the console and the program will either show the board after those moves have been completed or print the first invalid move entered.

Chess notation:  
Write moves in long algebraic notation.  
To move bishop from a1 to b2: Ba1-b2  
To capture a queen on b2: Ba1xQb2  
To capture a bishop en passen: a2xBb3ep  
To promote to queen: a7-a8=Q  
To castle: O-O  
If move delivers check write “+” at the end: e2-e3+  

Limits:  
Two issues with the program are:    
1) The program isn't that strict with move notation so it accepts all valid moves but doesn't reject all invalid moves. For example, if you said Ba1-b2 instead of Ba1xb2 when capturing the program will still accept that move.  
2) The program doesn't check for checkmates or stalemates and end the game if one occurs.  
