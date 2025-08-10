public class pow {
  public static long pow(int a, int b) {
    long result = 1;
    for (int i = 1; i <= b; i++) {
      result *= a;
    }
    return result;
  }
}
