#pragma once

#include <jni.h>

#ifdef __cplusplus
extern "C" {
#endif

JNIEXPORT jstring JNICALL Java_ru_startandroid_nativelab_MainActivity_stringFromJNI(JNIEnv* env, jclass clazz);

#ifdef __cplusplus
}
#endif