package by.sergey.sixth;

import android.app.Service;
import android.content.Intent;
import android.os.Binder;
import android.os.IBinder;
import android.util.Log;

import java.util.Timer;
import java.util.TimerTask;

public class MyService extends Service {
    final public static String LOG_TAG = "LOG";
    private int i = 0;
    MyBinder binder = new MyBinder();
    TimerTask tTask;
    Timer timer;

    public MyService() {
    }

    public void onCreate() {
        super.onCreate();
        Log.d(LOG_TAG, "onCreate");
        timer = new Timer();
    }

    public int onStartCommand(Intent intent, int flags, int startId) {
        Log.d(LOG_TAG, "onStartCommand");
        someTask();
        return super.onStartCommand(intent, flags, startId);
    }

    @Override
    public boolean onUnbind(Intent intent) {
        Log.d(LOG_TAG, "onUnbind");
        return super.onUnbind(intent);
    }

    public void onDestroy() {
        Log.d(LOG_TAG, "onDestroy");
        tTask.cancel();
        i=0;
        super.onDestroy();
    }

    @Override
    public IBinder onBind(Intent intent) {
        return binder;
    }

    public int getI(){
        return i;
    }

    private void someTask(){
        if (tTask != null) tTask.cancel();
        tTask = new TimerTask() {
            public void run() {
                i++;
            }
        };
        timer.schedule(tTask, 1000, 1000);
    }

    class MyBinder extends Binder {
        MyService getService() {
            return MyService.this;
        }
    }

}
