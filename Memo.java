public class Memo {
    public static int fib(int n){
        if (n <= 2){
            return 1;
        } else {
            return fib(n-1) + fib(n-2);
        }
    }
    public static int gT(int m, int n){
        if (m == 1 && n == 1){
            return 1;
        }if (m == 0 || n == 0){
            return 0;
        }else{
            return gT(m-1,n) + gT(m,n-1);
        }
    }
    public static int factorial(int n){
        if (n == 1){
            return 1;
        }else{
            return n * factorial(n-1);
        }
    }
    public static boolean canSum(int targetSum, int[] numbers){
        if (targetSum == 0){
            return true;
        }if (targetSum < 0){
            return false;
        }for (int i : numbers){
            int remainder = targetSum - i;
            if (canSum(remainder, numbers) == true){
                return true;
            }
        }return false;
    }
    public static void main(String[] args) {
    System.out.println("Fibinacci: ");
    System.out.println(fib(9));
    System.out.println("\n" + "gT: ");
    System.out.println(gT(2,5));
    System.out.println("factorial: ");
    System.out.println(factorial(7));
    System.out.println("canSum: ");
    System.out.println(canSum(7,{6,1}));
    }
}
