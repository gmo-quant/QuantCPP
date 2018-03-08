/* ===========================================================
|
|  
| 	 date: 2018-03-07 20:02:59
| Source code: Inequalities.cpp 
|      Author: Guangzhuan Mo
|
| Description:
|
| 	Input:
|
|      Output:
|
|     Process:
|	the program's steps are as follows:
|
|
| Known Bugs:
| 	None;
|	the program operates correctly
|
 * ===========================================================*/

#include "Inequalities.hpp"
// max and min of two numbers
double max(double x, double y)
{
	return x > y ? x : y;
}
double min(double x, double y)
{
	return x > y ? y : x;
}

// max and min of three numbers
double max(double x, double y, double z)
{
	return max(max(x, y), z);
}
double min(double x, double y, double z)
{
	return min(min(x, y), z);
}