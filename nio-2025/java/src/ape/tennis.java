package ape;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class tennis {
    private static Queue<String> inputQueue = new LinkedList<>();

    public static String readLine(BufferedReader reader) throws IOException {
        if (inputQueue.isEmpty()) {
            return reader.readLine();
        } else {
            return inputQueue.poll();
        }
    }

    public static void main(String[] args) throws IOException {
        inputQueue.add("19 5");
        inputQueue.add("BBABAAAABBAABBABBBB");
        inputQueue.add("1 2");
        inputQueue.add("1 4");
        inputQueue.add("3 2");
        inputQueue.add("4 2");
        inputQueue.add("5 2");


        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String line = readLine(reader);

        String[] parts = line.split(" ");
        int N = Integer.parseInt(parts[0]);
        int Q = Integer.parseInt(parts[1]);

        String S = readLine(reader);

        int[][] forslag = new int[Q][6];

        for (int i = 0; i < Q; i++) {
            parts = readLine(reader).split(" ");
            for (int j = 0; j < 2; j++) {
                forslag[i][j] = Integer.parseInt(parts[j]);
            }
            for (int j = 2; j < 6; j++) {
                forslag[i][j] = 0;
            }

        }
        System.out.println(Arrays.deepToString(forslag));

        int poeng_a = 0;
        int poeng_b = 0;

        int[] indexes = new int[Q];
        for (int i = 0; i < Q; i++) {
            indexes[i] = i;
        }

        for (int i = 0; i < N; i++) {
            char c = S.charAt(i);
            if (c == 'A') {
                poeng_a++;
            } else {
                poeng_b++;
            }
        }
    }
}
