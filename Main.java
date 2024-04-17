import javax.xml.transform.Source;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");

        System.out.println("-----Bienvenido------");
        System.out.print(("Ingrese el nombre de su red: "));
        Scanner scanner = new Scanner(System.in);
        String nombreRed = scanner.nextLine();
        ArrayList<Vlan> listaVlan = new ArrayList<>();
        boolean centinela = false;

        while (!centinela){
            System.out.println("-------------");
            System.out.println("1-Agregar Vlan");
            System.out.println("2-Agregar Pc");
            System.out.println("3-Agregar Switch");
            System.out.println("4-Borrar Vlan");
            System.out.println("5-Borrar Pc");
            System.out.println("6-Reporte");
            System.out.println("0-Salir");
            System.out.print("----->Indique su opción: ");
            String opcion = scanner.nextLine();
            int op = Integer.parseInt(opcion);

            switch (op){
                case 1:

                    Vlan nuevaVlan = new Vlan();
                    nuevaVlan.agregarVlan(listaVlan);

                    break;
                case 2:

                    break;
                case 3:

                    break;

                case 4:

                    break;
                case 5:

                    break;
                case 6:

                    break;

                case 0:
                    centinela = true;
                    break;

                default:
                    System.out.println("Opción inválida");
                    break;
            }
        }
        System.out.println("Usted ha salido del programa");
    }
}