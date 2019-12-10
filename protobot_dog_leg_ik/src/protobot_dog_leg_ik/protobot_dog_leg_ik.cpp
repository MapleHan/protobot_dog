#include <protobot_dog_leg_ik/protobot_dog_leg_ik.h>

Leg::Leg(char *name, bool dir)
{
	strcat(_name, name);
	_dir = dir;
	_middle[0] = 0;
	_middle[1] = 0;
}

void Leg::setDir(bool dir)
{
	_dir = dir;
}
bool Leg::getDir()
{
	return(_dir);
}

void Leg::setMiddle(int axis, float offset)
{
	_middle[axis] = offset;
}
float Leg::getMiddle(int axis)
{
	return _middle[axis];
}

void Leg::plotArea()
{
	float alpha, beta;
	for (float y = 0; y <= 2; y += 0.1)
	{
		for (float x = -2; x <= 2; x  += 0.1)
		{
			std::cout << cartesianToAlphaBeta(x, y, alpha, beta, _dir) << ' ';
		}
		std::cout << std::endl;
	}
	std::cout << std::endl;
}

int Leg::intersection(float x, float y, float &ix1, float &iy1, float &ix2, float &iy2)
{
	float d = sqrt(x * x + y * y);
	if (d == 0)
	{
		return 1;
	}
	if (d > 2)
	{
		return 2;
	}
	float a = d / 2.0;
	float h = sqrt(1 - a * a);
	float tx = a * x / d;
	float ty = a * y / d;
	ix1 = tx + h * y / d;
	iy1 = ty - h * x / d;
	ix2 = tx - h * y / d;
	iy2 = ty + h * x / d;
	return 0;
}

int Leg::cartesianToAlphaBeta(float x, float y, float &alpha, float &beta, bool dir)
{
	float ix1, iy1, ix2, iy2;
	if (!intersection(x, y, ix1, iy1, ix2, iy2))
	{
		float ix = ix1, iy = iy1;
		if (dir)
		{
			ix = ix2;
			iy = iy2;
		}
		alpha = atan2(iy, ix);
		if (alpha < 0) return 2;
		beta = atan2(y - iy, x - ix) - alpha;
		if (beta < -M_PI) beta += 2*M_PI;
		alpha -= M_PI/2;
		return 0;
	}
	if (x == 0 && y == 0)
	{
		alpha = 0;
		beta = M_PI;
		return 0;
	}
	return 1;
}
