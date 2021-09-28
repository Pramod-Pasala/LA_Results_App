package Loyola.CS.Result;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void submit(View v) {
        EditText uid=(EditText) findViewById(R.id.uid);
        String num=uid.getText().toString();
        if(num.length() !=12){
            Toast.makeText(getApplicationContext(),"Enter correct Uid", Toast.LENGTH_SHORT).show();
        }
        else{
            Intent getres = new Intent();
            getres.setClass(this,ResultScreen.class);
            getres.putExtra("uid",num);
            startActivity(getres);
        }

    }


}