public class aliquotSum {
    public static int aliquotSum(int number) {
        int sum = 0;
        for (int i = 1, limit = number / 2; i <= limit; ++i) {
            if (number % i == 0) {
                sum += i;
            }
        }
        return sum;
    }
}
