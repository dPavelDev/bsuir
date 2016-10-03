package by.sergey.lab5;

import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.GestureDetector;
import android.view.MotionEvent;
import android.view.View;

import com.mikepenz.materialdrawer.Drawer;

import by.sergey.lab5.utils.SwipeDetector;
import by.sergey.lab5.utils.Utils;

public class MainActivity extends FragmentActivity {
    GestureDetector gestureDetector;
    private Drawer.Result window = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        window = Utils.createCommonDrawer(MainActivity.this, null, null);
        window.setSelectionByIdentifier(1, true);

        gestureDetector = initGestureDetector();
        View view = findViewById(R.id.layout_1);
        view.setOnTouchListener(new View.OnTouchListener() {
            public boolean onTouch(View v, MotionEvent event) {
                return gestureDetector.onTouchEvent(event);
            }
        });
        view.setOnClickListener(new View.OnClickListener() {
            public void onClick(View arg0) {
            }
        });
    }

    @Override
    public void onBackPressed() {
        if (window.isDrawerOpen()) {
            window.closeDrawer();
        } else {
            super.onBackPressed();
        }
    }

    private GestureDetector initGestureDetector() {
        return new GestureDetector(new GestureDetector.SimpleOnGestureListener() {

            private SwipeDetector detector = new SwipeDetector();

            public boolean onFling(MotionEvent e1, MotionEvent e2, float velocityX,
                                   float velocityY) {
                try {
                    if (detector.isSwipeLeft(e1, e2, velocityX)) {
                        window.closeDrawer();
                    } else if (detector.isSwipeRight(e1, e2, velocityX)) {
                        window.openDrawer();
                    }
                } catch (Exception ignored) {}
                return false;
            }
        });
    }
}
