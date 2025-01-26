package drep.meg;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class tennis {
	public static String readLine(BufferedReader reader) throws IOException {
		return reader.readLine();
	}
	
	public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        // Reading data using readLine
        String name = readLine(reader);

        System.out.println(name);
	}
}
