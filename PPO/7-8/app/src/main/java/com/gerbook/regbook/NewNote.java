package com.gerbook.regbook;

import android.app.Activity;
import android.content.ContentValues;
import android.content.Context;
import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.os.Vibrator;
import android.util.Log;
import android.util.StringBuilderPrinter;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class NewNote extends Activity {

    DBhelper dBhelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.new_note);
        dBhelper = new DBhelper(this);
        findViewById(R.id.ok).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String name = String.valueOf(((EditText) findViewById(R.id.name)).getText());
                String number = String.valueOf(((EditText) findViewById(R.id.number)).getText());
                if (name.equals("") || number.equals("")){
                    Toast.makeText(view.getContext(), "Write data!", Toast.LENGTH_SHORT).show();
                } else {
                    if (check_number(view, number)) {
                        add_database(name, number);
                        Intent intent = new Intent(NewNote.this, MainActivity.class);
                        startActivity(intent);
                    }
                }
            }
        });
    }

    public boolean check_number(View v, String number){
        MyNDK d = new MyNDK();
        if (String.valueOf(d.validate(number)).equals("good")){
            return true;
        }
        else {
            Toast.makeText(v.getContext(), d.validate(number), Toast.LENGTH_SHORT).show();
            return false;
        }
    }
    public void add_database(String name, String number){
        SQLiteDatabase database = dBhelper.getReadableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(dBhelper.KEY_NAME, name);
        contentValues.put(dBhelper.KEY_NUMBER, number);
        contentValues.put(dBhelper.KEY_COUNT, 0);

        database.insert(dBhelper.TABLE_BOOK, null, contentValues);
    }
}
