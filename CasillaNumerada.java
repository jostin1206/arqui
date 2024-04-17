public class CasillaNumerada extends Casilla {
    public int bombasCercanas;

    public CasillaNumerada(int bombasCercanas) {
        this.setBombasCercanas(bombasCercanas);
    }

    @Override
    public void mostrar() {
        if(this.esRevelado()) {
            System.out.print(getBombasCercanas() + " ");
        } else {
            System.out.print("ℹ ");
        }
    }

    public int getBombasCercanas() {
        return bombasCercanas;
    }

    public void setBombasCercanas(int bombasCercanas) {
        this.bombasCercanas = bombasCercanas;
    }
}
