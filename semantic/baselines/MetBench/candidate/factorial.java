public class factorial {
  public static long factorial(int n) {
    if (n < 0) {
      throw new IllegalArgumentException("number is negative");
    }
    long factorial = 1;
    for (int i = 1; i <= n; factorial *= i, ++i);
    return factorial;
  }
}
