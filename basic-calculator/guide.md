## en_GB
To generate a random number, first **make sure to either**
- open a *fresh instance* of this app
- reset ALL using **C button**

If done correctly - current output should be 0.
Now follow these instructions:
1. Press the **CE button** which instead of clearing the text will begin the generation proces.
2. Type in the first bounding number ([x,])
3. Press the **= button**
4. Type in the second bounding number ([x,y])
5. Press **= button** again

The generated number will be seen in the output field. It can be used for further calculations!
If you wish too, pressing **= button** again will generate another number within previously set boundaries.

### Important!
The random generator picks a number between first and second, including them.
It is also sensitive for decimal values.
Examples :
- [1, 6] generates a random integer from 1 to 6. (simulates a dice roll)
- [10, -5] works just like previous example; order doesn't matter.
- [0.0, 1.0] generates a random number from 0 to 1 with one number after the decimal point. (e.g 0.1, 0.7, 1.0)
- [0.0, 9.999] the amount of numbers afther the decimal point is always determined by the maximal length from either boundaries. (e.g 0.000, 2.115, 4.020)
- [-10, 10.0001] works just like previous example even though the first number has no decimal value.
