import java.util.Scanner;

public class Twins {
    
    private static boolean Prime(long num) {
		if (num < 2)
			return false;
		if (num == 2)
			return true;
		if (num % 2 == 0)
			return false;
		for (int i = 3; i * i <= num; i += 2)
			if (num % i == 0)
				return false;
		return true;
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		long n = in.nextLong();
		long m = in.nextLong();
		in.close();

		int count = 0;

		for (long i = n; i <= m - 2; i++) {
			if (Prime(i)) {
				if (Prime(i + 2)) {
					count++;
				}
			}
		}

		System.out.println(count);
	}
}

