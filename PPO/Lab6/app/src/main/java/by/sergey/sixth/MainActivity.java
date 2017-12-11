package by.sergey.sixth;

import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.IBinder;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    Button start, stop, fetch;
    TextView text;
    MyService myService;
    boolean bound = false;
    ServiceConnection sConn;
    Intent intent;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        CreateViews();
        SetListeners();
        intent = new Intent(this, MyService.class);
        sConn = new ServiceConnection() {

            public void onServiceConnected(ComponentName name, IBinder binder) {
                myService = ((MyService.MyBinder) binder).getService();
                bound = true;
            }

            public void onServiceDisconnected(ComponentName name) {
                bound = false;
            }
        };
        bindService(intent, sConn, BIND_AUTO_CREATE);
    }

    private void CreateViews(){
        start = (Button)findViewById(R.id.start);
        stop = (Button)findViewById(R.id.stop);
        fetch = (Button)findViewById(R.id.fetch);
        text = (TextView)findViewById(R.id.text);
    }

    private void SetListeners(){
        start.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startService();
            }
        });
        stop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                stopService();
            }
        });
        fetch.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setText();
            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        bindService(intent, sConn, 0);
    }

    @Override
    protected void onStop() {
        super.onStop();
        if (!bound) return;
        unbindService(sConn);
        bound = false;
    }

    private void startService(){
        startService(intent);
    }

    private void stopService(){
        stopService(intent);
        myService.onDestroy();
    }

    private void setText(){
        text.setText(String.valueOf(myService.getI()));
    }

}
