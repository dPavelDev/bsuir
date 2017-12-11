package com.gerbook.regbook;

import android.content.Context;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Vibrator;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private DBhelper dbHelper;
    private SQLiteDatabase database;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        dbHelper = new DBhelper(this);
        dbHelper.getWritableDatabase();
        database = dbHelper.getWritableDatabase();
        findViewById(R.id.add).setX(30);
        findViewById(R.id.add).setY(1300);
        findViewById(R.id.add).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, NewNote.class);
                startActivity(intent);
            }
        });

        display_contact();
    }

    public void display_contact(){
        Cursor cursor = database.query(dbHelper.TABLE_BOOK, null, null, null, null, null, null);
        if (cursor.moveToFirst()){
            int index_name = cursor.getColumnIndex(dbHelper.KEY_NAME);
            int index_number = cursor.getColumnIndex(dbHelper.KEY_NUMBER);

            while (cursor.moveToNext()){
                add_row(cursor.getString(index_name), cursor.getString(index_number));
            }
        }
        cursor.close();
    }

    public void add_row(final String name, final String number){

        final LayoutInflater inflater = this.getLayoutInflater();
        final TableLayout table = (TableLayout)findViewById(R.id.table);
        TableRow tr = (TableRow) inflater.inflate(R.layout.table_row, null);
        tr.setClickable(true);

        tr.setOnLongClickListener(new View.OnLongClickListener() {
            @Override
            public boolean onLongClick(View view) {
                database.delete(dbHelper.TABLE_BOOK, dbHelper.KEY_NAME + "=? and " + dbHelper.KEY_NUMBER + "=?",
                        new String[]{name, number});
               // Toast.makeText(getActivity().getApplicationContext(), "Delete from database", Toast.LENGTH_SHORT).show();
                table.removeView(view);
                return true;
            }
        });

        TextView txt = (TextView) tr.findViewById(R.id.little_mes);
        txt.setText(name+":"+'\n'+number);
        table.addView(tr);
    }
}
