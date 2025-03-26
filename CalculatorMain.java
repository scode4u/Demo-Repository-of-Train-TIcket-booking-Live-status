import java.util.Scanner;

public class CalculatorMain {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter first number: ");
        double num1 = scanner.nextDouble();

        System.out.println("Enter second number: ");
        double num2 = scanner.nextDouble();

        System.out.println("Select operation: +, -, *, /");
        char operation = scanner.next().charAt(0);

        double result = 0;
        boolean valid = true;

        switch (operation) {
            case '+':
                result = Addition.add(num1, num2);
                break;
            case '-':
                result = Subtraction.subtract(num1, num2);
                break;
            case '*':
                result = Multiplication.multiply(num1, num2);
                break;
            case '/':
                try {
                    result = Division.divide(num1, num2);
                } catch (ArithmeticException e) {
                    System.out.println(e.getMessage());
                    valid = false;
                }
                break;
            default:
                System.out.println("Invalid operation selected.");
                valid = false;
        }

        if (valid) {
            System.out.println("Result: " + result);
        }

        scanner.close();
    }
}
