/* ===========================================================
|
|  
| 	 date: 2018-03-07 20:02:59
| Source code: InequalitiesTester.cpp 
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
#include<iostream>
using namespace std;
#include "Inequalities.hpp"
#include "DatasimDate.hpp"

int main()
{
	double d1, d2;
	cout << "first double";
	cin >> d1;
	cout << "second double";
	cin >> d2;
	cout << "max is : " << max(d1, d2) << endl;
	cout << "min is : " << min(d1, d2) << endl;
}