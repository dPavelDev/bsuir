package by.sergey.lab5.utils;

import android.view.MotionEvent;

public class SwipeDetector {

    private int swipe_distance;
    private int swipe_velocity;
    private static final int SWIPE_DISTANCE = 120;
    private static final int SWIPE_VELOCITY = 200;

    public SwipeDetector() {
        super();
        this.swipe_distance = SWIPE_DISTANCE;
        this.swipe_velocity = SWIPE_VELOCITY;
    }

    public boolean isSwipeLeft(MotionEvent e1, MotionEvent e2, float velocityX) {
        return isSwipe(e1.getX(), e2.getX(), velocityX);
    }

    public boolean isSwipeRight(MotionEvent e1, MotionEvent e2, float velocityX) {
        return isSwipe(e2.getX(), e1.getX(), velocityX);
    }

    private boolean isSwipeDistance(float coordinateA, float coordinateB) {
        return (coordinateA - coordinateB) > this.swipe_distance;
    }

    private boolean isSwipeSpeed(float velocity) {
        return Math.abs(velocity) > this.swipe_velocity;
    }

    private boolean isSwipe(float coordinateA, float coordinateB, float velocity) {
        return isSwipeDistance(coordinateA, coordinateB)
                && isSwipeSpeed(velocity);
    }
}
