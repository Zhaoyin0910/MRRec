private double[] fst(double[] f) {
        if (!ArithmeticUtils.isPowerOfTwo(f.length)) {
            throw new TransformException(TransformException.NOT_POWER_OF_TWO,
                                         f.length);
        }
        if (f[0] != 0) {
            throw new TransformException(TransformException.FIRST_ELEMENT_NOT_ZERO,
                                         f[0]);
        }

        final double[] transformed = new double[f.length];
        final int n = f.length;
        if (n == 1) {
            transformed[0] = 0;
            return transformed;
        }

        // construct a new array and perform FFT on it
        final double[] x = new double[n];
        x[0] = 0;
        final int nShifted = n >> 1;
        x[nShifted] = 2 * f[nShifted];
        final double piOverN = Math.PI / n;
        for (int i = 1; i < nShifted; i++) {
            final int nMi = n - i;
            final double fi = f[i];
            final double fnMi = f[nMi];
            final double a = Math.sin(i * piOverN) * (fi + fnMi);
            final double b = 0.5 * (fi - fnMi);
            x[i] = a + b;
            x[nMi] = a - b;
        }

        final FastFourierTransform transform = new FastFourierTransform(FastFourierTransform.Norm.STD);
        final Complex[] y = transform.apply(x);

        // reconstruct the FST result for the original array
        transformed[0] = 0;
        transformed[1] = 0.5 * y[0].getReal();
        for (int i = 1; i < nShifted; i++) {
            final int i2 = 2 * i;
            transformed[i2] = -y[i].getImaginary();
            transformed[i2 + 1] = y[i].getReal() + transformed[i2 - 1];
        }

        return transformed;
    }