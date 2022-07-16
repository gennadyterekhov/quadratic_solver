import java.lang.Math;
class QuadraticSolver {
    public static void main(String[] args) {
        double coefA = 0;
        double coefB = 0;
        double coefC = 0;
        double divisor = 0;
        double radixBody = 0;

        if (args.length != 3) {
            System.out.printf("Expect 3 parameters, found %d\n", args.length);
            System.exit(1);
        }

        try {
            coefA = Double.parseDouble(args[0]);
            coefB = Double.parseDouble(args[1]);
            coefC = Double.parseDouble(args[2]);
        } catch(Exception exception) {
            System.out.println("parameters must be of type int or double");
            System.exit(1);
        }

        if (coefA == 0.0) {
            double root1 = -coefC / coefB;
            System.out.printf("root : %f\n", root1);
            System.exit(0);
        }

        radixBody = coefB * coefB - 4 * coefA * coefC;
        divisor = 2 * coefA;

        if (radixBody < 0) {
            System.out.println("discriminant is negative, solution lies in complex numbers");
            System.exit(0);
        }

        double root1 = (-coefB + Math.sqrt(radixBody)) / divisor;
        double root2 = (-coefB - Math.sqrt(radixBody)) / divisor;

        System.out.printf("root 1: %f\n", root1);
        System.out.printf("root 2: %f\n", root2);
    }
}