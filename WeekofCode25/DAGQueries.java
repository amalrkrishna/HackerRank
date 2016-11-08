import java.util.*;

public class Dag {
    
    private Map<Integer, List<Integer>> graph = new HashMap<>();
    private BitSet vstd;
    private int[] data;
    public static void main(String[] args)
    {
          new Dag().Solve();
    }

    public void Solve() {
        Scanner scanner = new Scanner(System.in);
        int v = scanner.nextInt();
        int e = scanner.nextInt();
        int q = scanner.nextInt();

        vstd = new BitSet(v+1);
        vstd.clear();
        data = new int[v+1];

        for (int i = 0; i < e; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            if (!graph.containsKey(a)) {
                graph.put(a, new ArrayList<Integer>());
            }
            graph.get(a).add(b);
        }

        while (q-- > 0) {
            int query = scanner.nextInt();
            int a, b;
            switch (query) {
                case 1:
                    a = scanner.nextInt();
                    b = scanner.nextInt();
                    vstd.clear();
                    All(a, b, vstd);
                    break;
                case 2:
                    a = scanner.nextInt();
                    b = scanner.nextInt();
                    vstd.clear();
                    Small(a, b, vstd);
                    break;
                case 3:
                    a = scanner.nextInt();
                    System.out.println(data[a]);
                    break;
            }
        }
        scanner.close();
    }

    private void Small (int u, int s, BitSet vstd) {
        vstd.set(u);
        if (data[u] > s) data[u] = s;

        if (graph.containsKey(u)) {
            for (int n : graph.get(u)) {
                if (!vstd.get(n)) Small(n, s, vstd);
            }
        }
    }

    private void All (int u, int s, BitSet vstd) {
        vstd.set(u);
        data[u] = s;

        if (graph.containsKey(u)) {
            for (int n : graph.get(u)) {
                if (!vstd.get(n)) All(n, s, vstd);
            }
        }
    }
}
