private static void quadMult(final double[] a, final double[] b, final double[] result) {
        final double[] xs = new double[2];
        final double[] ys = new double[2];
        final double[] zs = new double[2];

        /* a[0] * b[0] */
        split(a[0], xs);
        split(b[0], ys);
        splitMult(xs, ys, zs);

        result[0] = zs[0];
        result[1] = zs[1];

        /* a[0] * b[1] */
        split(b[1], ys);
        splitMult(xs, ys, zs);

        double tmp = result[0] + zs[0];
        result[1] -= tmp - result[0] - zs[0];
        result[0] = tmp;
        tmp = result[0] + zs[1];
        result[1] -= tmp - result[0] - zs[1];
        result[0] = tmp;

        /* a[1] * b[0] */
        split(a[1], xs);
        split(b[0], ys);
        splitMult(xs, ys, zs);

        tmp = result[0] + zs[0];
        result[1] -= tmp - result[0] - zs[0];
        result[0] = tmp;
        tmp = result[0] + zs[1];
        result[1] -= tmp - result[0] - zs[1];
        result[0] = tmp;

        /* a[1] * b[0] */
        split(a[1], xs);
        split(b[1], ys);
        splitMult(xs, ys, zs);

        tmp = result[0] + zs[0];
        result[1] -= tmp - result[0] - zs[0];
        result[0] = tmp;
        tmp = result[0] + zs[1];
        result[1] -= tmp - result[0] - zs[1];
        result[0] = tmp;
    }