package pid43;

/**
 * 43. Multiply Strings
 * Given two numbers represented as strings, return multiplication of the
 * numbers as a string.
 * 
 * Note: The numbers can be arbitrarily large and are non-negative. Converting
 * the input string to integer is NOT allowed. You should NOT use internal
 * library such as BigInteger. Subscribe to see which companies asked this
 * question
 * 
 * @author ��
 *
 */
public class main {
	public static void main(String[] args) {
		String[][] numTable = { { "123", "456" }, { "789", "987" }, {
				"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890",
				"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" },

				{ "00010", "00100" }, { "0", "1" }, { "0", "2" }, { "0", "3" }, { "0", "4" }, };
		for (String[] ito : numTable) {
			test(ito[0], ito[1]);
		}
	}

	private static void test(String num1, String num2) {
		Solution solution = new Solution();
		String rtn = solution.multiply(num1, num2);
		System.out.println(rtn);
		System.out.println("-------------");
	}
}