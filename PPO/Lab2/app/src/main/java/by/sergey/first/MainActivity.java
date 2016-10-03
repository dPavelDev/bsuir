package by.sergey.first;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

import java.util.LinkedList;

import by.sergey.calc.Calc;

public class MainActivity extends AppCompatActivity {
    TextView textView = (TextView) null;
    Calc calc = new Calc();
    LinkedList<Button> digits = new LinkedList<>();
    LinkedList<Button> operations = new LinkedList<>();
    Button delButton;
    Button equalButton;
    Button changeButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        textView = (TextView) findViewById(R.id.textField);

        createViews();
        setListeners();

        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
    }

    void clickDeleteOperation() {
        textView.setText(calc.deleteDigit());
    }

    void clickNumber(String digit) {
        textView.setText(calc.addDigit(digit));
    }

    void clickOperation(String operation) {
        if (calc.getNumber().length() > 0) {
            if (calc.setOperation(operation)) {
                textView.setText(calc.getNumber());
            }
        }
    }

    void clickEqual() {
        if (calc.getNumber().length() > 0) {
            if (calc.setEqual()) {
                textView.setText(calc.getNumber());
            }
        }
    }

    void clickChangeSign() {
        if (calc.getNumber().length() > 0) {
            textView.setText(calc.changeSign());
        }
    }

    void createViews() {
        int[] buttons_id = new int[]{R.id.button0, R.id.button1, R.id.button2, R.id.button3,
                R.id.button4, R.id.button5, R.id.button6, R.id.button7, R.id.button8,
                R.id.button9};
        int[] operation_buttons_id = new int[]{R.id.operation_button_plus,
                R.id.operation_button_minus, R.id.operation_button_dup,
                R.id.operation_button_div};

        for (int aButtons_id : buttons_id) {
            Button b = (Button) findViewById(aButtons_id);
            digits.add(b);
        }
        for (int aButtons_id : operation_buttons_id) {
            Button b = (Button) findViewById(aButtons_id);
            operations.add(b);
        }
        delButton = (Button) findViewById(R.id.operation_button_del);
        equalButton = (Button) findViewById(R.id.operation_button_equal);
        changeButton = (Button) findViewById(R.id.operation_button_change);
    }

    void setListeners() {
        OnClickListener onClickBtn = new OnClickListener() {
            @Override
            public void onClick(View v) {
                clickNumber(String.valueOf(((Button) v).getText()));
            }
        };
        OnClickListener onClickOperationBtn = new OnClickListener() {
            @Override
            public void onClick(View v) {
                clickOperation(String.valueOf(((Button) v).getText()));
            }
        };
        OnClickListener onClickDelBtn = new OnClickListener() {
            @Override
            public void onClick(View v) {
                clickDeleteOperation();
            }
        };
        OnClickListener onClickEqualBtn = new OnClickListener() {
            @Override
            public void onClick(View v) {
                clickEqual();
            }
        };
        OnClickListener onClickChangeBtn = new OnClickListener() {
            @Override
            public void onClick(View v) {
                clickChangeSign();
            }
        };
        for (Button button : digits) {
            button.setOnClickListener(onClickBtn);
        }
        for (Button button : operations) {
            button.setOnClickListener(onClickOperationBtn);
        }
        delButton.setOnClickListener(onClickDelBtn);
        equalButton.setOnClickListener(onClickEqualBtn);
        changeButton.setOnClickListener(onClickChangeBtn);
    }
}
