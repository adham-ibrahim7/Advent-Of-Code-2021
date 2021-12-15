import java.util.*;
import java.io.*;

public class Day15 {
    public static void main(String[] args) throws IOException {
        setIn("day15.txt");
        setOut();

        N = 100;
        int[][] orig = new int[N][N];
        for (int i = 0; i < N; i++) {
            String line = rl();
            for (int j = 0; j < N; j++) {
                orig[i][j] = line.charAt(j) - '0';
            }
        }

        List<Pair> pairs = new LinkedList<>();
        Map<Pair, Edge> edges = new HashMap<>();
        for (int k = 0; k < 5; k++) {
            for (int u = 0; u < N; u++) {

            }
        }

        apsp(orig);

        closeIO();
    }

    static int N;

    private static class Edge {
        Pair u, v;
        int weight;
        Edge(Pair u, Pair v, int weight) {
            this.u = u;
            this.v = v;
            this.weight = weight;
        }
    }

    private static class Pair {
        int i, j;
        Pair(int i, int j) {
            this.i = i;
            this.j = j;
        }

        @Override
        public boolean equals(Object o) {
            if (!(o instanceof Pair)) return false;
            Pair p = (Pair) o;
            return this.i == p.i && this.j == p.j;
        }

        @Override
        public int hashCode() {
            return i * 31 + j;
        }
    }

    private static Pair PR(int i, int j) {
        return new Pair(i, j);
    }

    private static List<Pair> pairs(int[][] weights) {
        List<Pair> pairs = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                pairs.add(PR(i, j));
            }
        }
        return pairs;
    }

    private static Map<Pair, List<Edge>> edges(int[][] weights) {
        Map<Pair, List<Edge>> adj = new HashMap<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                Pair p = PR(i, j);

                adj.putIfAbsent(p, new LinkedList<>());
                if (i > 0) {
                    adj.get(p).add(new Edge(p, PR(i-1, j), weights[i-1][j]));
                }

                if (j > 0) {
                    adj.get(p).add(new Edge(p, PR(i, j-1), weights[i][j-1]));
                }

                if (i < N-1) {
                    adj.get(p).add(new Edge(p, PR(i+1, j), weights[i+1][j]));
                }

                if (j < N-1) {
                    adj.get(p).add(new Edge(p, PR(i, j+1), weights[i][j+1]));
                }
            }
        }

        return adj;
    }

    private static Map<Pair, Integer> dijkstra(Pair src, List<Pair> pairs, Map<Pair, List<Edge>> adj) {
        Map<Pair, Integer> dist = new HashMap<>();
        PriorityQueue<Pair> pq = new PriorityQueue<>((a, b) -> {
            if (Objects.equals(dist.get(a), dist.get(b))) {
                if (a.i == b.i) {
                    return a.j - b.j;
                }
                return a.i - b.i;
            }
            return dist.get(a) - dist.get(b);
        });

        for (Pair u : pairs) {
            int INF = 100000;
            dist.put(u, u.equals(src) ? 0 : INF);
            pq.add(u);
        }

        while (!pq.isEmpty()) {
            Pair u = pq.remove();
//            System.out.println(u.i + " " + u.j);
            for (Edge e : adj.get(u)) {
                relax(e, dist, pq);
            }
        }

        return dist;
    }

    private static void relax(Edge e, Map<Pair, Integer> dist, PriorityQueue<Pair> pq) {
        int i = e.u.i;
        int j = e.u.j;
        int k = e.v.i;
        int h = e.v.j;

//        for (Pair p : dist.keySet()) {
//            out.println(p.i + " " + p.j);
//        }

        int dprime = dist.get(PR(i, j)) + e.weight;
        if (dprime < dist.get(PR(k, h))) {
            pq.remove(e.v);
            dist.put(PR(k, h), dprime);
            pq.add(e.v);
        }
    }

    private static Map<Pair, Integer>[][] apsp(int[][] weights) {
        // 0 top 1 left 2 bottom 3 right
        Map<Pair, Integer>[][] dist = new Map[4][N];

        List<Pair> pairs = pairs(weights);
        Map<Pair, List<Edge>> edges = edges(weights);

        for (int u = 0; u < N; u++) {
            dist[0][u] = dijkstra(PR(0, u), pairs, edges);
            dist[1][u] = dijkstra(PR(u, 0), pairs, edges);
            dist[2][u] = dijkstra(PR(N-1, u), pairs, edges);
            dist[3][u] = dijkstra(PR(u, N-1), pairs, edges);
            System.out.println(u);
        }

        return dist;
    }

    static BufferedReader f;
    static PrintWriter out;
    static StringTokenizer st;

    static final int MOD = 1000000007;

    static String rl() throws IOException {
        return f.readLine();
    }

    static int ni(StringTokenizer st) {
        return Integer.parseInt(st.nextToken());
    }

    static long nlg(StringTokenizer st) {
        return Long.parseLong(st.nextToken());
    }

    static int ni() throws IOException {
        return Integer.parseInt(rl());
    }

    static long nlg() throws IOException {
        return Long.parseLong(rl());
    }

    static StringTokenizer nl() throws IOException {
        return new StringTokenizer(rl());
    }

    static int[] nia(int N) throws IOException {
        StringTokenizer st = nl();
        int[] A = new int[N];
        for (int i = 0; i < N; i++)
            A[i] = ni(st);
        return A;
    }

    static void setIn(String s) throws IOException {
        f = new BufferedReader(new FileReader(s));
    }

    static void setOut(String s) throws IOException {
        out = new PrintWriter(new FileWriter(s));
    }

    static void setIn() {
        f = new BufferedReader(new InputStreamReader(System.in));
    }

    static void setOut() {
        out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    }

    static void setIO(String s) throws IOException {
        setIn(s + ".in");
        setOut(s + ".out");
    }

    static void setTextIO(String s) throws IOException {
        setIn(s + ".txt");
        setOut(s + "_out.txt");
    }

    static void setIO() {
        setIn();
        setOut();
    }

    static void closeIO() throws IOException {
        f.close();
        out.close();
    }
}