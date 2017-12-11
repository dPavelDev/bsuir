package com.gerbook.regbook;

import java.util.ArrayList;
import java.util.HashMap;

public class MyNDK  {

    static {
        System.loadLibrary("MyLibrary");
    }

    public native String validate(String a);
}
