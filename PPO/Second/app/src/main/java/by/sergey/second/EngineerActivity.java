package by.sergey.second;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.LinkedList;

import by.sergey.calc.EngineerCalc;

public class EngineerActivity extends AppCompatActivity {
    EngineerCalc calc;
    TextView textView;
    LinkedList<Button> digits = new LinkedList<>();
    LinkedList<Button> operations = new LinkedList<>();
    LinkedList<Button> unaryOperations = new LinkedList<>();
    Button delButton;
    Button equalButton;
    Button changeButton;
    Button dotButton;
    Button stepToNormal;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.engineer);
        textView = (TextView)findViewById(R.id.textField);
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

    private void clickUnaryOperation(String operation) {
        if (calc.getNumber().length() > 0) {
            if (calc.UnaryOperation(operation)) {
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

    private void startMainActivity(){
        Intent intent = new Intent(this, MainActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
        startActivity(intent);
    }

    private void createViews() {
        int[] buttonsIds = new int[] {
            R.id.button0, R.id.button1, R.id.button2, R.id.button3,
            R.id.button4, R.id.button5, R.id.button6, R.id.button7,
            R.id.button8, R.id.button9
        };

        int[] operationButtonsIds = new int[] { R.id.operation_button_pow };

        int[] unaryOperationButtonsIds = new int[] {
            R.id.operation_button_sin,
            R.id.operation_button_cos,
            R.id.operation_button_tan,
            R.id.operation_button_sqrt
        };

        for (int buttonId : buttonsIds) {
            Button b = (Button) findViewById(buttonId);
            digits.add(b);
        }
        for (int buttonId : operationButtonsIds) {
            Button b = (Button) findViewById(buttonId);
            operations.add(b);
        }
        for (int buttonId : unaryOperationButtonsIds) {
            Button b = (Button) findViewById(buttonId);
            unaryOperations.add(b);
        }

        delButton = (Button) findViewById(R.id.operation_button_del);
        equalButton = (Button) findViewById(R.id.operation_button_equal);
        changeButton = (Button) findViewById(R.id.operation_button_change);
        dotButton= (Button) findViewById(R.id.operation_button_dot);
        stepToNormal = (Button)findViewById(R.id.stepToNormal);
    }

    private void setListeners() {
        View.OnClickListener onClickBtn = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clickNumber(String.valueOf(((Button) v).getText()));
            }
        };
        View.OnClickListener onClickOperationBtn = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clickOperation(String.valueOf(((Button) v).getText()));
            }
        };
        View.OnClickListener onClickUnaryOperationBtn = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clickUnaryOperation(String.valueOf(((Button) v).getText()));
            }
        };
        View.OnClickListener onClickDelBtn = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clickDelOperation();
            }
        };
        View.OnClickListener onClickEqualBtn = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clickEqual();
            }
        };
        View.OnClickListener onClickChangeBtn = new View.OnClickListener() {
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
        for (Button button : unaryOperations) {
            button.setOnClickListener(onClickUnaryOperationBtn);
        }
        delButton.setOnClickListener(onClickDelBtn);
        dotButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clickAddDot();
            }
        });
        equalButton.setOnClickListener(onClickEqualBtn);
        changeButton.setOnClickListener(onClickChangeBtn);
        stepToNormal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startMainActivity();
            }
        });
    }
}
