import java.util.Scanner;

public class Main {


    public static void main(String[] args) {
        System.out.println("Hello world!");

        System.out.println("---------------------------------------");
        System.out.println("  Bienvenidos al juego del buscaminas");
        System.out.println("---------------------------------------");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el ancho de la mina: ");
        String ancho = scanner.nextLine();
        int numFilas = Integer.parseInt(ancho);

        System.out.print("Ingrese el largo de la mina: ");
        String largo = scanner.nextLine();
        int numColumnas = Integer.parseInt(largo);
        Tablero tablero = new Tablero();
        tablero.mostrarTablero(numFilas,numColumnas);

        //System.out.print("Ingrese la cantidad de bombas a colocar: ");
        //int cantBombas = Integer.parseInt(scanner.nextLine());

        tablero.mostrarBombas();

    }
}