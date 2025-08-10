public class perfectCube {
  public static boolean perfectCube(int number) {
    int a = (int) Math.pow(number, 1.0 / 3);
    return a * a * a == number;
  }
}
