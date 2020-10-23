public class Money {
  private int dollars;
  private int cents;

  public Money (int dollars, int cents) {
    this.dollars = dollars;
    this.cents = cents;
  }

  public void add (Money moreMoney) {
    cents = cents + moreMoney.cents;
    if (cents >= 100) {
      cents = cents - 100;
     dollars++;
    }
    dollars = dollars + moreMoney.dollars;
  }

  public String toString () {
    return "$" + dollars + "." + (cents <= 9 ? "0" : "") + cents;
  }

  public static void main (String[] args) {
    Money m1 = new Money(5, 30);
    Money m2 = new Money(6, 13);

    m1.add(m2);
    System.out.println("Total is " + m1);
  }
}
