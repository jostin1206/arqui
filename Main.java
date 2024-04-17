import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("--------------------------------------------------");
        System.out.println("                    Bienvenido                    ");
        System.out.println("--------------------------------------------------");
        System.out.println("Ingrese el ancho incial de la mina");
        int anch = sc.nextInt();
        System.out.println("Ingrese el largo incial de la mina");
        int lar = sc.nextInt();
        System.out.println("Ingrese el numero maximo de intentos");
        int max_bomb = sc.nextInt();
        System.out.println("");
        System.out.println("Estado inicial de la mina:");
        System.out.println("");
        Tablero tabl = new Tablero(lar, anch, max_bomb);
        tabl.mostrarTablero();
        System.out.println("");
        System.out.println("Ingrese la cantidad de bombas a colocar:");
        int bomb = sc.nextInt();
        System.out.println("");
        System.out.println("Ingrese las coordenadas de las bombas");

        int[][] matriz = new int[tabl.filas][tabl.columnas];
        for(int i = 0; i < tabl.filas; i++){
            for(int j = 0; j < tabl.columnas; j++){
                matriz[i][j] = 0;
            }
        }
        int[] vecx = {1, 1, 1, 0, 0, -1, -1, -1};
        int[] vecy = {-1, 1, 0, 1, -1, 1, 0, -1};
        int cont = 1;

        for(int i = 0; i < bomb; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            Casilla cas = new Casilla();
            tabl.casillas[x][y] = cas;
            matriz[x][y] = 9;
            for(int k = 0; k < 8; k++){
                if(x + vecx[k] < tabl.filas && x + vecx[k] >= 0 && y + vecy[k] < tabl.filas && y + vecy[k] >= 0) matriz[x + vecx[k]][y + vecy[k]]++;
            }
        }

        for(int i = 0; i < tabl.filas; i++){
            for(int j = 0; j < tabl.columnas; j++){
                if(matriz[i][j] == 0){
                    CasillaSegura cas1 = new CasillaSegura();
                    tabl.casillas[i][j] = cas1;
                } else if(matriz[i][j] > 0  && matriz[i][j] < 9){
                    CasillaNumerada cas2 = new CasillaNumerada(matriz[i][j]);
                    tabl.casillas[i][j] = cas2;
                } else {
                    CasillaBomba cas3 = new CasillaBomba();
                    tabl.casillas[i][j] = cas3;
                }


            }
        }

        for (int i = 0; i < tabl.filas; i++){
            for (int j = 0; j < tabl.columnas; j++){
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println("");
        }

        int contador_bombas = 0;
        while(true){
            System.out.println("Ingrese la posicion (x,y) de la mina en su intento numero:" + cont);
            int x = sc.nextInt();
            int y = sc.nextInt();
            tabl.casillas[x][y].revelar();
            if(matriz[x][y] == 0){
                int lol = 1;
                int lol_pas = lol;
                int[][] ga = new int[1000][2];
                ga[0][0] = x;
                ga[0][1] = y;
                while(lol > 0){
                    lol = 0;
                    for(int i = 0; i < lol_pas; i++){
                        for(int k = 0; k < 8; k++){
                            int x1 = ga[i][0] + vecx[k];
                            int y1 = ga[i][1] + vecy[k];
                            if(x1 < tabl.filas && x1 >= 0 && y1 < tabl.filas && y1 >= 0 && !tabl.casillas[x1][y1].esRevelado()){
                                if(matriz[x1][y1] == 0){
                                    ga[lol][0] = x1;
                                    ga[lol][1] = y1;
                                    tabl.casillas[x1][y1].revelar();
                                    lol++;
                                } else {
                                    tabl.casillas[x1][y1].revelar();
                                }
                            }
                        }
                    }
                    lol_pas = lol;
                }
            } else tabl.casillas[x][y].revelar();


            tabl.mostrarTablero();

            if(matriz[x][y] > 8) {
                contador_bombas++;
                int tqm = max_bomb - contador_bombas;
                if(tqm > 0) System.out.println("Encontro una bomba, le queda(n) " + tqm + " intento(s) !");
            }
            if(contador_bombas >= max_bomb){
                System.out.println("Has perdido el juego!");
                System.exit(0);
            }
            System.out.println("");
            if(tabl.ganoJuego(bomb)) {
                System.out.println("Has ganado el juego!");
                System.exit(0);
            }

        }


    }
}
