import java.util.*;
import java.io.*;

public class Day15 {
    public static void main(String[] args) throws IOException {
        setIn("day15.txt");
        setOut("day15_out.txt");

        N = 100;
        int[][] orig = new int[N][N];
        for (int i = 0; i < N; i++) {
            String line = rl();
            for (int j = 0; j < N; j++) {
                orig[i][j] = line.charAt(j) - '0';
            }
        }

        List<Pair> pairs = new LinkedList<>();
        Map<Pair, List<Edge>> edges = new HashMap<>();

        int K = 5;
        for (int f = 0; f < K; f++) {
            for (int g = 0; g < K; g++) {
                List<Pair> curr = new LinkedList<>();
                for (int i = f * N; i < (f+1) * N; i++) {
                    // left
                    curr.add(PR(i, g * N));
                    // right
                    curr.add(PR(i, (g+1) * N - 1));
                }

                for (int j = g * N; j < (g+1) * N; j++) {
                    // top
                    curr.add(PR(f * N, j));
                    // bottom
                    curr.add(PR((f+1) * N - 1, j));
                }

                Map<Pair, Map<Pair, Integer>> dists = apsp(orig, f + g);
                System.out.println("Computed f=" + f + ", g=" + g);

                for (int i = 0; i < curr.size(); i++) {
                    for (int j = 0; j < curr.size(); j++) {
                        Pair a = curr.get(i);
                        Pair b = curr.get(j);

                        Pair c = PR(a.i % N, a.j % N);
                        Pair d = PR(b.i % N, b.j % N);

                        edges.putIfAbsent(a, new LinkedList<>());
                        edges.get(a).add(new Edge(a, b, dists.get(c).get(d)));
                    }
                }

                for (Pair p : curr) {
                    edges.putIfAbsent(p, new LinkedList<>());

                    int i = p.i % N;
                    int j = p.j % N;

                    if (i == 0 && f > 0) {
                        int w = (orig[N-1][j] + (f-1) + g - 1) % 9 + 1;
                        edges.get(p).add(new Edge(p, PR(p.i-1, p.j), w));
                    }

                    if (j == 0 && g > 0) {
                        int w = (orig[i][N-1] + f + (g-1) - 1) % 9 + 1;
                        edges.get(p).add(new Edge(p, PR(p.i, p.j-1), w));
                    }

                    if (i == N-1 && f < K-1) {
                        int w = (orig[0][j] + (f+1) + g - 1) % 9 + 1;
                        edges.get(p).add(new Edge(p, PR(p.i+1, p.j), w));
                    }

                    if (j == N-1 && g < K-1) {
                        int w = (orig[i][0] + f + (g+1) - 1) % 9 + 1;
                        edges.get(p).add(new Edge(p, PR(p.i, p.j+1), w));
                    }
                }

                pairs.addAll(curr);
            }
        }

        Map<Pair, Integer> dist = dijkstra(PR(0, 0), pairs, edges);
        out.println("part 2: " + dist.get(PR(K*N-1, K*N-1)));
        System.out.println("part 2: " + dist.get(PR(K*N-1, K*N-1)));

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

    private static Map<Pair, List<Edge>> edges(int[][] weights, int offset) {
        Map<Pair, List<Edge>> adj = new HashMap<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                Pair p = PR(i, j);

                adj.putIfAbsent(p, new LinkedList<>());
                if (i > 0) {
                    adj.get(p).add(new Edge(p, PR(i-1, j), (weights[i-1][j] + offset - 1) % 9 + 1));
                }

                if (j > 0) {
                    adj.get(p).add(new Edge(p, PR(i, j-1), (weights[i][j-1] + offset - 1) % 9 + 1));
                }

                if (i < N-1) {
                    adj.get(p).add(new Edge(p, PR(i+1, j), (weights[i+1][j] + offset - 1) % 9 + 1));
                }

                if (j < N-1) {
                    adj.get(p).add(new Edge(p, PR(i, j+1), (weights[i][j+1] + offset - 1) % 9 + 1));
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

        int w = e.weight;

        int dprime = dist.get(PR(i, j)) + w;
        if (dprime < dist.get(PR(k, h))) {
            pq.remove(e.v);
            dist.put(PR(k, h), dprime);
            pq.add(e.v);
        }
    }

    private static Map<Pair, Map<Pair, Integer>> apsp(int[][] weights, int offset) {
        // 0 top 1 left 2 bottom 3 right
        Map<Pair, Map<Pair, Integer>> dist = new HashMap<>();

        List<Pair> pairs = pairs(weights);
        Map<Pair, List<Edge>> edges = edges(weights, offset);

        for (int u = 0; u < N; u++) {
            for (Pair p : new Pair[] {PR(0, u), PR(u, 0), PR(N-1, u), PR(u, N-1)}) {
                dist.put(p, dijkstra(p, pairs, edges));
            }

//            dist[0][u] = dijkstra(PR(0, u), pairs, edges);
//            dist[1][u] = dijkstra(PR(u, 0), pairs, edges);
//            dist[2][u] = dijkstra(PR(N-1, u), pairs, edges);
//            dist[3][u] = dijkstra(PR(u, N-1), pairs, edges);
//            System.out.println(u);
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