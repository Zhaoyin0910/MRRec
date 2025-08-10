public class ceil {
  public static double ceil(double number) {
    if (number - (int) number == 0) {
      return number;
    } else if (number - (int) number > 0) {
      return (int) (number + 1);
    } else {
      return (int) number;
    }
  }
}
