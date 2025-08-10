private double[] fct(double[] f) {
        final int n = f.length - 1;
        if (!ArithmeticUtils.isPowerOfTwo(n)) {
            throw new TransformException(TransformException.NOT_POWER_OF_TWO_PLUS_ONE,
                                         Integer.valueOf(f.length));
        }

        final double[] transformed = new double[f.length];

        if (n == 1) {       // trivial case
            transformed[0] = 0.5 * (f[0] + f[1]);
            transformed[1] = 0.5 * (f[0] - f[1]);
            return transformed;
        }

        // construct a new array and perform FFT on it
        final double[] x = new double[n];
        x[0] = 0.5 * (f[0] + f[n]);
        final int nShifted = n >> 1;
        x[nShifted] = f[nShifted];
        // temporary variable for transformed[1]
        double t1 = 0.5 * (f[0] - f[n]);
        final double piOverN = Math.PI / n;
        for (int i = 1; i < nShifted; i++) {
            final int nMi = n - i;
            final double fi = f[i];
            final double fnMi = f[nMi];
            final double a = 0.5 * (fi + fnMi);
            final double arg = i * piOverN;
            final double b = Math.sin(arg) * (fi - fnMi);
            final double c = Math.cos(arg) * (fi - fnMi);
            x[i] = a - b;
            x[nMi] = a + b;
            t1 += c;
        }
        final FastFourierTransform transformer = new FastFourierTransform(FastFourierTransform.Norm.STD,
                                                                          false);
        final Complex[] y = transformer.apply(x);

        // reconstruct the FCT result for the original array
        transformed[0] = y[0].getReal();
        transformed[1] = t1;
        for (int i = 1; i < nShifted; i++) {
            final int i2 = 2 * i;
            transformed[i2] = y[i].getReal();
            transformed[i2 + 1] = transformed[i2 - 1] - y[i].getImaginary();
        }
        transformed[n] = y[nShifted].getReal();

        return transformed;
    }