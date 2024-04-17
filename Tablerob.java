public class Tablero {
    public Casilla[][] casillas;
    public int intentosRestantes;

    public int filas;
    public int columnas;

    public Tablero(int filas, int columnas, int intentosRestantes) {
        this.filas = filas;
        this.columnas = columnas;
        casillas = new Casilla[filas][columnas];
        for (int i = 0; i < filas; i++){
            for (int j = 0; j < columnas; j++){
                casillas[i][j] = new Casilla();
            }
        }

        this.intentosRestantes = intentosRestantes;
    }

    public void mostrarTablero() {
        for (int i = 0; i < filas; i++){
            for (int j = 0; j < columnas; j++){
                casillas[i][j].mostrar();
            }
            System.out.println("");
        }
    }

    public boolean ganoJuego(int bombas){
        int cont = 0;
        int total = filas*columnas - bombas;
        for(int i = 0; i < filas; i++){
            for(int j = 0; j < columnas; j++){
                if(casillas[i][j].esRevelado()) cont++;
            }
        }
        if (cont >= total) return true;
        else return false;


    }

}

