public class CasillaBomba extends Casilla {
    @Override
    public void mostrar() {
        if(this.esRevelado()) {
            System.out.print("☸ ");
        } else {
            System.out.print("ℹ ");
        }
    }
}
