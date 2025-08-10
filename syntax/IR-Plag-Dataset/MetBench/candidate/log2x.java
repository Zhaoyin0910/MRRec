public class log2x {
        public static double log2x(double x) {
            if (x <= 0) {
                throw new IllegalArgumentException("Input must be positive");
            }
    
            int exponent = 0;
            while (x >= 2.0) {
                x /= 2.0;
                exponent++;
            }
    
            double mantissa = x - 1.0;
            double mantissaSquared = mantissa * mantissa;
            double sum = 0.0;
            double term = mantissa;
            double denominator = 1.0;
            int n = 1;
    
            while (Math.abs(term) > 1e-15) {
                sum += term / denominator;
                term *= -mantissaSquared;
                denominator++;
                n++;
            }

            return exponent + sum;
        }
    }
    