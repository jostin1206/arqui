import java.util.ArrayList;
import java.util.Scanner;

public class Vlan{
    private String nombre;
    private boolean permiteCorreo;
    private boolean permiteFacebook;
    private boolean permiteWow;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public boolean isPermiteCorreo() {
        return permiteCorreo;
    }

    public void setPermiteCorreo(boolean permiteCorreo) {
        this.permiteCorreo = permiteCorreo;
    }

    public boolean isPermiteFacebook() {
        return permiteFacebook;
    }

    public void setPermiteFacebook(boolean permiteFacebook) {
        this.permiteFacebook = permiteFacebook;
    }

    public boolean isPermiteWow() {
        return permiteWow;
    }

    public void setPermiteWow(boolean permiteWow) {
        this.permiteWow = permiteWow;
    }
    public Vlan(){

    }
    public Vlan(String nombre, boolean permiteCorreo, boolean permiteFacebook, boolean permiteWow) {
        this.nombre = nombre;
        this.permiteCorreo = permiteCorreo;
        this.permiteFacebook = permiteFacebook;
        this.permiteWow = permiteWow;
    }

    public void agregarVlan(ArrayList<Vlan> listaVlan){
        System.out.print("Ingrese el nombre de la Vlan: ");
        Scanner scanner = new Scanner(System.in);
        String nombre = scanner.nextLine();

        boolean existe = false;

        for(Vlan vlan:listaVlan){
            if(vlan.getNombre().equals(nombre)){

                existe = true;
                break;
            }

        }
        if(existe){
            System.out.println("La vlan ya existe");
        }
        else{

            System.out.print("¿Permite Correo? (S/N): ");
            String pCorreo = scanner.nextLine();
            boolean validar1 = false;
            while(!validar1){

                if(pCorreo.equals("S") ||pCorreo.equals("s") ||pCorreo.equals("N") ||pCorreo.equals("n")  ){

                    validar1 = true;

                }
                else{
                    System.out.print("Entrada no válida, vuelva a ingresar ");
                    pCorreo = scanner.nextLine();
                }

            }
            System.out.print("¿Permite Facebook? (S/N): ");
            String pFacebook = scanner.nextLine();
            boolean validar2 = false;

            while(!validar2){

                if(pFacebook.equals("S") ||pFacebook.equals("s") ||pFacebook.equals("N") ||pFacebook.equals("n")){

                    validar2 = true;
                }
                else{
                    System.out.print("Entrada no válida, vuelva a ingresar ");
                    pFacebook = scanner.nextLine();
                }

            }

            System.out.print("¿Permite Wow? (S/N): ");
            String pWow = scanner.nextLine();
            boolean validar3 = false;

            while(!validar3){

                if(pWow.equals("S") ||pWow.equals("s") ||pWow.equals("N") ||pWow.equals("n")){

                    validar3 = true;
                }
                else{
                    System.out.print("Entrada no válida, vuelva a ingresar ");
                    pWow = scanner.nextLine();
                }
            }
            System.out.println("-----Vlan agregada------");

            Vlan nuevaVlan = new Vlan(nombre, pCorreo.equals("S"), pFacebook.equals("S"), pWow.equals("S"));

            listaVlan.add(nuevaVlan);
        }
    }
}
