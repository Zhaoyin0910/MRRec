public class cot {
    public static double cot(double x) {
        // 调整x到[-π, π]区间
        x = x % (2 * Math.PI);
        if (x < -Math.PI) {
            x += 2 * Math.PI;
        } else if (x > Math.PI) {
            x -= 2 * Math.PI;
        }

        // 处理x为0或π的极端情况
        if (Math.abs(x) < 1e-10 || Math.abs(x - Math.PI) < 1e-10 || Math.abs(x + Math.PI) < 1e-10) {
            return Double.NaN; // cot(0)和cot(±π)无定义
        }

        // 计算cos和sin的泰勒展开
        double cos = calculateCos(x);
        double sin = calculateSin(x);

        return cos / sin;
    }

    private static double calculateCos(double x) {
        double cos = 1;
        double term = 1;
        int sign = -1;
        for (int i = 2; i <= 40; i += 2) {
            term *= x * x / (i * (i - 1));
            cos += sign * term;
            sign *= -1;
        }
        return cos;
    }

    private static double calculateSin(double x) {
        double sin = x;
        double term = x;
        for (int i = 1; i < 20; i++) {
            term *= -x * x / ((2 * i) * (2 * i + 1));
            sin += term;
        }
        return sin;
    }
}