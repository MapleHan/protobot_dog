#ifndef _LEG_H_
#define _LEG_H_
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>

class Leg
{
	public:
		Leg(char *name="default leg", bool dir = 0);
		void setDir(bool dir);
		bool getDir();
		void setMiddle(int axis, float offset);
		float getMiddle(int axis);
		void plotArea();
		int cartesianToAlphaBeta(float x, float y, float &alpha, float &beta, bool dir = 0);
	private:
		char _name[20];
		float _middle[2];
		bool _dir;
		int intersection(float x, float y, float &ix1, float &iy1, float &ix2, float &iy2);
};
#endif
