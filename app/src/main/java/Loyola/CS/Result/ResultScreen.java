package Loyola.CS.Result;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class ResultScreen extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_result_screen);

        if (! Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }
        Python py=Python.getInstance();
        PyObject pyobj =py.getModule("result");
        PyObject obj =pyobj.callAttr("");

    }
}