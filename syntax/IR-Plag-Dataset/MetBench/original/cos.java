public class cos {
    public static double cos(double x) {
        x = x % (2 * Math.PI);
        if (x < -Math.PI) {
            x += 2 * Math.PI;
        } else if (x > Math.PI) {
            x -= 2 * Math.PI;
        }
        double result = 1;
        double term = 1;
        int sign = -1;
        double factorial = 1;
        for (int i = 2; i <= 20; i += 2) {
            term *= x * x / (i * (i - 1));
            factorial *= i * (i - 1);
            result += sign * term;
            sign = -sign;
        }
        return result;
    }
}
