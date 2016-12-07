import java.util.Scanner;

public class MusicOnTheStreet {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int a[]=new int[n];
		for (int i = 0; i < n; i++) {
			a[i]=in.nextInt();
		}
		int m=in.nextInt();
		int hmin=in.nextInt();
		int hmax=in.nextInt();

		int start=a[0]-hmax;
		int count=hmax;
		for (int i = 1; i < a.length; i++) {
			if(count>=m)
			{
				System.out.println(start);
				System.exit(-1);
			}
			if(a[i]-a[i-1]>=hmin && a[i]-a[i-1]<=hmax)
			{

				count+=a[i]-a[i-1];
			}
			else{
				count+=Math.min(hmin, hmax);
				if(count>=m)
				{
					System.out.println(start);
					System.exit(-1);
				}
				start=a[i]-hmax;
			}
		}
		System.out.println(start);
	}
}
