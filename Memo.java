public class Memo {
    public static void main(String[] args) {
    int result = fib(9);
    System.out.println(result);
    }
    public static int fib(int n){
        if (n <= 2){
            return 1;
        } else {
            return fib(n-1) + fib(n-2);
        } 
    }
}
