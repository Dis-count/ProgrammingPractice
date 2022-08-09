package Template96;

public class Main {
    public static void main(String[] args) {
		int[] testTable = { 0, 1, 2, 3, 4, 5, 6, 10 };
		for (int input : testTable) {
			test(input);
		}
    }
    private static void test(int input) {
        Solution solution = new Solution();
        int output;
        long begin = System.currentTimeMillis();
        output = solution.numTrees(input);
        long end = System.currentTimeMillis();
        System.out.println(input + ":	output= " + output);
        System.out.println();
        System.out.println("Used time:" + (end - begin) + "ms");
        System.out.println("-------------------");
    }
}
