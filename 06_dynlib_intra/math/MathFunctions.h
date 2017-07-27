#ifndef POWER_H
#define POWER_H

#if defined _WIN32
	#if MATH_BUILD
                #define MATH_API __declspec(dllexport)
        #else
                #define MATH_API __declspec(dllimport)
        #endif
#else
    #define MATH_API
#endif

MATH_API double power(double base, int exponent);

#endif
