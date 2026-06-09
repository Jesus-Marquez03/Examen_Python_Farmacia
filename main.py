import modules.ui.mainMenu as menu
import utils.functions as functions

if __name__ == "__main__":
    try:

        functions.eliminar()
        menu.mainMenu()

    except KeyboardInterrupt:

        functions.eliminar()

        print("\nCierre forzado por el usuario (Ctrl+C). ¡Hasta luego!\n")

    except Exception as e:

        functions.eliminar()

        print("==========================================")
        print(f"ERROR INESPERADO DEL SISTEMA: {e}")
        print("==========================================")