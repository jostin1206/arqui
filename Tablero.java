import java.util.Scanner;

public class Tablero {
    private int numFilas;
    private int numColumnas;

   // public Tablero(int numFilas, int numColumnas) {

     //   this.numFilas = numFilas;
       // this.numColumnas = numColumnas;

    //}

    public int getNumFilas() {
        return numFilas;
    }

    public void setNumFilas(int numFilas) {
        this.numFilas = numFilas;
    }

    public int getNumColumnas() {
        return numColumnas;
    }

    public void setNumColumnas(int numColumnas) {
        this.numColumnas = numColumnas;
    }

    public void mostrarTablero(int numFilas,int numColumnas){

        System.out.println("Estado inicial de la mina");
        String [][] matriz = new String[numFilas][numColumnas];

        for(int i=0;i<numFilas;i++){

            for(int j=0;j<numColumnas;j++){

                matriz[i][j] = "ℹ";

            }
        }
        for(int i=0;i<numFilas;i++){
            for(int j=0;j<numColumnas;j++){
                System.out.print(matriz[i][j]+"");
            }
            System.out.println();
        }
    }

    public void mostrarBombas(){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese la cantidad de bombas a colocar: ");
        int cantBombas = Integer.parseInt(scanner.nextLine());
        System.out.print("Ingrese las coordenadas de las bombas: ");
        for(int k=1;k<=cantBombas;k++){
            int x = Integer.parseInt(scanner.nextLine());
            int y = Integer.parseInt(scanner.nextLine());

            System.out.print("("+ x + "," + y + ")");
        }


    }

}
