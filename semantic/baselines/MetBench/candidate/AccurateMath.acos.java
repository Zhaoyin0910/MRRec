public static double acos(double x) {
    if (Double.isNaN(x)) {
        return Double.NaN;
    }

    if (x > 1.0 || x < -1.0) {
        return Double.NaN;
    }

    if (x == -1.0) {
        return Math.PI;
    }

    if (x == 1.0) {
        return 0.0;
    }

    if (x == 0) {
        return Math.PI / 2.0;
    }

    boolean isNegative = x < 0;
    double absX = Math.abs(x);
    double result;

    // 使用不同的展开方式根据x的绝对值大小
    if (absX <= 0.7071) {
        result = taylorSeries(absX);
    } else {
        // 使用针对接近1的展开式，利用acos(x) = 2 * asin(sqrt((1-x)/2))，但此处使用特定的级数展开
        double t = 1.0 - absX;
        result = sqrt2tSeries(t);
    }

    // 处理负数情况
    if (isNegative) {
        result = Math.PI - result;
    }

    return result;
}

// 原点处的泰勒级数展开，适用于|x| <= 0.7071
private static double taylorSeries(double x) {
    double sum = 0.0;
    double term = x;
    int n = 0;
    final double epsilon = 1e-15;
    double xSquared = x * x;

    while (Math.abs(term) > epsilon) {
        sum += term;
        n++;
        double factor = ((2 * n - 1) * (2 * n - 1)) / (2.0 * n * (2 * n + 1)) * xSquared;
        term *= factor;
    }

    return Math.PI / 2.0 - sum;
}

// 接近1时的级数展开，适用于x > 0.7071，计算acos(x) = sqrt(2*t) * sum，其中t = 1 - x
private static double sqrt2tSeries(double t) {
    double sqrt2t = Math.sqrt(2 * t);
    double sum = 1.0;
    double term = 1.0;
    int k = 1;
    final double epsilon = 1e-15;

    while (true) {
        double factorNumerator = (2 * k - 1) * (2 * k - 1);
        double factorDenominator = 2 * k * (2 * k + 1);
        double factor = (factorNumerator / factorDenominator) * t;
        term *= factor;

        sum += term;

        if (Math.abs(term) <= epsilon) {
            break;
        }

        k++;
    }

    return sqrt2t * sum;
}