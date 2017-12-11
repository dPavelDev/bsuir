#include "com_gerbook_regbook_MyNDK.h"
#include <stdio.h>
#include <string.h>

JNIEXPORT jstring JNICALL Java_com_gerbook_regbook_MyNDK_validate(JNIEnv* env, jobject, jstring a) {
    const char *nativeString = env->GetStringUTFChars(a, JNI_FALSE);

    int length = strlen(nativeString);

    if (length > 13){
        return env->NewStringUTF("Too long");
    }
    if (length < 13){
        return env->NewStringUTF("Too short");
    }
    return env->NewStringUTF("good");
}

