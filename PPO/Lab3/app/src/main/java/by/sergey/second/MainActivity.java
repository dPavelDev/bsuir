package by.sergey.second;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

import java.util.LinkedList;

import by.sergey.calc.EngineerCalc;

public class MainActivity extends AppCompatActivity {
    TextView textView = (TextView) null;
    EngineerCalc calc = null;
    LinkedList<Button> digits = new LinkedList<>();
    LinkedList<Button> operations = new LinkedList<>();
    Button delButton;
    Button equalButton;
    Button changeButton;
    Button dotButton;
    Button stepToEngineer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        textView = (TextView) findViewById(R.id.textField);
        calc = EngineerCalc.getCalc();
        textView.setText(calc.getNumber());
        createViews();
        setListeners();
    }

    private void clickDelOperation() {
        textView.setText(calc.deleteDigit());
    }

    private void clickNumber(String digit) {
        textView.setText(calc.addDigit(digit));
    }

    private void clickOperation(String operation) {
        if (calc.getNumber().length() > 0) {
            if (calc.setOperation(operation)) {
                textView.setText(calc.getNumber());
            }
        }
    }

    private void clickEqual() {
        if (calc.getNumber().length() > 0) {
            if (calc.setEqual()) {
                textView.setText(calc.getNumber());
            }
        }
    }

    private void clickChangeSign() {
        if (calc.getNumber().length() > 0) {
            textView.setText(calc.changeSign());
        }
    }

    private void clickAddDot() {
        if (calc.getNumber().length() > 0) {
            textView.setText(calc.addDot());
        }
    }

    private void startEngineerActivity(){
        Intent intent = new Intent(this, EngineerActivity.class);
        //TODO: wtf
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
        startActivity(intent);
    }

    private void createViews() {
        int[] buttonsIds = new int[] {
            R.id.button0, R.id.button1, R.id.button2, R.id.button3,
            R.id.button4, R.id.button5, R.id.button6, R.id.button7,
            R.id.button8, R.id.button9
        };

        int[] operationButtonsIds = new int[] {
            R.id.operation_button_plus,
            R.id.operation_button_minus, R.id.operation_button_dup,
            R.id.operation_button_div
        };

        for (int buttonId : buttonsIds) {
            Button b = (Button) findViewById(buttonId);
            digits.add(b);
        }

        for (int buttonId : operationButtonsIds) {
            Button b = (Button) findViewById(buttonId);
            operations.add(b);
        }

        delButton = (Button) findViewById(R.id.operation_button_del);
        equalButton = (Button) findViewById(R.id.operation_button_equal);
        changeButton = (Button) findViewById(R.id.operation_button_change);
        dotButton= (Button) findViewById(R.id.operation_button_dot);
        stepToEngineer = (Button) findViewById(R.id.stepToEngineer);
    }

    private void setListeners() {
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
                clickDelOperation();
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
        OnClickListener onClickStepBtn = new OnClickListener() {
            @Override
            public void onClick(View v) {
                startEngineerActivity();
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
        dotButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clickAddDot();
            }
        });
        stepToEngineer.setOnClickListener(onClickStepBtn);
    }
}
