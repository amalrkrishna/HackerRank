import java.util.Scanner;

public class cuttingtool {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int q = in.nextInt();
        StringBuffer s = new StringBuffer();
        for(int a0 = 0; a0 < q; a0++){
            int n = in.nextInt();
            long m = ((long)n)*2;
            long p = m*(m+1)/2+1-m;
            s.append(p+"\n");
        }
        System.out.println(s);
    }
}
