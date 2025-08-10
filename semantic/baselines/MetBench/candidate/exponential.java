public class exponential {
    public static double exponential(double x) {
        // 泰勒展开式：e^x = 1 + x/1! + x^2/2! + x^3/3! + … 
        double result = 1;
        double term = 1;
        double factorial = 1;
        for (int i = 1; i <= 20; i++) {
            term *= x / i;
            factorial *= i; // 这里与代码一类似地计算阶乘，虽然在计算中已隐含在 term 的更新中
            result += term;
        }
        return result;
    }
}
