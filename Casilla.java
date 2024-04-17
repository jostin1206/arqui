public class Casilla {
    public boolean revelado;

    public Casilla() {
        this.revelado = false;
    }

    public void mostrar(){
        System.out.print("ℹ ");
    };

    public boolean esRevelado() {
        return revelado;
    }

    public void revelar() {
        revelado = true;
    }
}
