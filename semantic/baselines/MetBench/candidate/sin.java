public class sin {
    public static double sin(double x) {
        x = x % (2 * Math.PI);
        if (x < -Math.PI) {
            x += 2 * Math.PI;
        } else if (x > Math.PI) {
            x -= 2 * Math.PI;
        }
        boolean negative = false;
        if (x < 0) {
            x = -x;
            negative = true;
        }
        if (x > Math.PI / 2) {
            x = Math.PI - x;
        }
        double result = x;
        double term = x;
        int sign = -1;
        for (int i = 2; i <= 20; i += 2) {
            term *= x * x / (i * (i + 1));
            result += sign * term;
            sign = -sign;
        }
        return negative ? -result : result;
    }
}