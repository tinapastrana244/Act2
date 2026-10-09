package ejercicio2.pkg1;

public class Persona {

    String nombre;
    String apellido;
    String númeroDocumentoIdentidad;
    int añoNacimiento;
    String PaisNacimiento;
    char género;

    // Metodo constructor de una persona
    Persona(String nombre, String apellido,
            String númeroDocumentoIdentidad,
            int añoNacimiento, String PaisNacimiento,
            char género) {

        this.nombre = nombre;
        this.apellido = apellido;
        this.númeroDocumentoIdentidad = númeroDocumentoIdentidad;
        this.añoNacimiento = añoNacimiento;
        this.PaisNacimiento = PaisNacimiento;
        this.género = género;
    }

    // Metodo que imprime en pantalla los datos de una persona
    void imprimir() {

        System.out.println("Nombre = " + nombre);
        System.out.println("Apellido = " + apellido);
        System.out.println("Número de documento de identidad = "
                + númeroDocumentoIdentidad);
        System.out.println("Año de nacimiento = " + añoNacimiento);
        System.out.println("País de nacimiento = " + PaisNacimiento);
        System.out.println("género = " + género);
        System.out.println();
    }
}
