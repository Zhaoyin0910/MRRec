public class log {
    public static double log(double x) {
        if (x <= 0) {
            throw new IllegalArgumentException("Input must be greater than 0");
        }

        // 将 x 调整到泰勒展开收敛区间 (0.5 < m <= 1)
        int exponent = Math.getExponent(x);
        double m = Math.scalb(x, -exponent); // 分解为 m * 2^exponent
        if (m < 0.5) {
            m *= 2;
            exponent--;
        }

        // 泰勒展开变量替换: u = m - 1
        double u = m - 1;
        double result = 0;
        double term = u;
        int sign = 1;

        // 泰勒展开式: ln(1+u) = u - u²/2 + u³/3 - u⁴/4 + ...
        for (int i = 1; i <= 20; i++) {
            result += sign * term / i;
            term *= u;
            sign = -sign;
        }

        // 加上指数部分: ln(x) = ln(m) + exponent * ln(2)
        result += exponent * 0.6931471805599453; // 预计算 ln(2)
        return result;
    }
}