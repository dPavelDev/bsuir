#include <android/log.h>
#include <string>
#include "nativelab.h"

JNIEXPORT jstring JNICALL Java_ru_startandroid_nativelab_MainActivity_stringFromJNI(JNIEnv* env, jclass clazz)
{
    std::string jniMessage("Hello NDK!");
    return env->NewStringUTF(jniMessage.c_str());
}


