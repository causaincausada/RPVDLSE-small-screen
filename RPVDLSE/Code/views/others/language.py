class Language:
    def __init__(self):
        # Spanish Language default
        # words and texts in the tabs
        self.results = "Resultados"
        self.gallery = "Galería"

        # words and texts in the menu bar
        self.menubar_results_label = 'Resultados'
        self.restore = 'Restaurar'
        self.backup = "Respaldar"
        self.settings = "Configuración"
        self.spanish = "Español"
        self.english = "Ingles"
        self.language = "Lenguaje"
        self.local_camera = "Camara local"
        self.ip_camera = "Ip camara"
        self.camera = "Camara"
        self.try_connect = "Intentar conectar Base de datos"
        self.restore_menu_file_label = 'Restaurar desde un archivo'
        self.restore_menu_initiate_label = 'Restaurar a estado inicial'

        # words camera ip
        self.protocol = "Protocolo"
        self.user = "Usuario"
        self.password = "Contraseña"
        self.ip = "Ip"
        self.port = "Puerto"
        self.ext = "Extras"
        self.protection = "Protegido"
        self.confirm = "Confirmar"
        self.cancel = "Cancelar"

        # word and texts in the galery window
        self.open = "Abrir"
        self.delete = "Eliminar"
        self.rename = "Renombrar"
        self.recognize = "Reconocer"
        self.internals = "Internas"
        self.externals = "Externas"

        # words and texts in the result window
        self.result = "Resultado"
        self.filters_title = "Filtros de búsqueda"
        self.date = "Fecha"
        self.hour = "Hora"
        self.begin = "Inicio"
        self.end = "Fin"
        self.name = "Nombre"
        self.name_image = "Nombre de la imagen"
        self.num_results = "Núm. resultados"
        self.plate = "Placa" 
        self.plate_results = "(Resultados del análisis)"
        
        # words ant texts in the camara module
        self.title_camera = "Cámara"
        
        # Messages Alerts
        self.message_error_img_location = "La imagen ya no se encuentra en la ubicación, el sistema va a refrescar" \
                                          " la galería."
        self.message_error_img_location_title = "Error: ubicación de la imagen"
        # Delete image
        self.message_confirm_delete_img = "¿Desea eliminar la imagen: {}?"
        self.message_confirm_delete_img_title = "Eliminar imagen"
        self.message_ok_delete = "La imagen se eliminó correctamente."
        self.message_ok_delete_title = "Imagen eliminada"
        # Rename image
        self.message_rename = "Introduce un nuevo nombre para la imagen. (Solo letras y números)."
        self.message_rename_title = "Renombrar imagen"
        self.rename_ok = "El nombre se ha cambiado correctamente."
        self.no_valid_name = "El nombre ingresado no es válido."

        # Recognition image
        self.message_recognition_complete_title = "Reconocimiento completo"
        self.message_recognition_complete_text = "La imagen se reconoció correctamente\nResultado: {}"
        self.error_database_title = "Error con base de datos"
        self.error_database_text = "Ocurrió un error al comunicarse con la base de datos.\n" \
                                   "Resultado no almacenado.\nResultado: {}"

        # Messages Backup
        self.message_confirm_backup_title = "Confirmación de respaldo"
        self.message_confirm_backup_text = "Se ha realizado correctamente \nel respaldo de resultados"
        self.message_error_backup_title = "Error al realizar respaldo"
        self.message_error_backup_text = "Error en la base de datos\nEl sistema no logró realizar el " \
                                         "respaldo de los resultados.\n\nVuelva intentar, si el problema persiste " \
                                         "intente iniciar la base de datos nuevamente\n " \
                                         "en el apartado de ajustes del menú bar"
        self.ask_confirm_backup_title = "Confirmación respaldar"
        self.ask_confirm_backup_text1 = "¿Desea respaldar el estado actual de resultados?\nResutlados:"
        self.ask_confirm_backup_text2 = "\nEl archivo será guardado bajo el nombre de: \n"

        # Messages Restore
        self.ask_confirm_restore_title = "Confirmación restaurar"
        self.ask_confirm_restore_text = "¿Desea continuar?\nAl restaurar este archivo se perderán todos los\n" \
                                        "resultados que no hayan sido respaldados\ncon anterioridad"
        self.Message_confirm_restore_title = "Confirmación de restauración"
        self.Message_confirm_restore_text = "Se ha realizado correctamente la\nrestauración de resultados"
        self.Message_error_restore_title = "Error al restaurar"
        self.Message_error_restore_text = "ARCHIVO CORRUPTO O INEXISTENTE\nEl sistema no logro realizar la " \
                                          "restauración de los\nresultados.\n\nVuelva intentar, si el problema " \
                                          "persiste restaure otro\n archivo de resultados, o restaure a estado inicial."

        # Messages Camera
        self.message_error_camera_title = "Error en módulo de cámara"
        self.message_error_camera_text = "Fallo en la conexión con la cámara"

        # Messages Data Base
        self.mes_error_connect_db_title = "Fallo conexión BD"
        self.mes_error_connect_db_text = "Fallo en la conexión con la base de datos"

        # Messages main Window
        self.ask_confirm_close_main_title = "Cerrar ventana principal"
        self.ask_confirm_close_main_text = "Esta por cerrar la ventana principal, ¿desea continuar?"

        # Warnings messages
        self.warning_date = "La fecha de inicio supera la fecha de fin"
        self.warning_hour_inversed = "La hora de inicio supera la hora de fin"
        self.warning_hour_invalid = "El formato de una hora es incorrecto\n Formato ejemplo: 13:00 "
        self.warning_invalid_plate_name = "El formato de la placa es incorrecto\n Caracteres permitidos: A-Za-z0-9_ -"
        self.warning_invalid_name = "El formato de nombre es incorrecto\n Caracteres permitidos: A-Za-z0-9_ -"

        # New rute cam
        self.error_rute_title = "Error en la ruta"
        self.error_rute_text = "Faltan datos por ingresar "

    def language_change(self, num_language):
        if num_language == 0:
            # English Language
            # words and texts in the tabs
            self.results = "Results"
            self.gallery = "Gallery"

            # words and texts in the menu bar
            self.menubar_results_label = 'Results'
            self.restore = 'Restore'
            self.backup = "Backup"
            self.settings = "settings"
            self.spanish = "Spanish"
            self.english = "English"
            self.language = "Language"
            self.local_camera = "Local camera"
            self.ip_camera = "Ip camera"
            self.camera = "Camera"
            self.try_connect = "Try to connect database"
            self.restore_menu_file_label = 'Restore from a file'
            self.restore_menu_initiate_label = 'Restore to initial state'

            # words camera ip
            self.protocol = "Protocol"
            self.user = "User"
            self.password = "Password"
            self.ip = "Ip"
            self.port = "Port"
            self.ext = "Args"
            self.protection = "Protection"
            self.confirm = "Confirm"
            self.cancel = "Cancel"
            
            # word and texts in the gallery window
            self.open = "Open"
            self.delete = "Delete"
            self.rename = "Rename"
            self.recognize = "Recognize"
            self.internals = "Internals"
            self.externals = "Externals"

            # words and texts in the result window
            self.result = "Result"
            self.filters_title = "Search filters"
            self.date = "Date"
            self.hour = "Hour"
            self.begin = "Begin"
            self.end = "End"
            self.name = "Name"
            self.name_image = "Image name"
            self.num_results = "Num of results"
            self.plate = "Plate" 
            self.plate_results = "(Analysts results)"
            
            # words ant texts in the camara module
            self.title_camera = "Camera"

            # Messages Alerts
            self.message_error_img_location = "The image is no longer in the location, the system will " \
                                              "refresh the gallery."
            self.message_error_img_location_title = "Error: image location"
            # Delete image
            self.message_confirm_delete_img = "Do you want to delete the image: {}?"
            self.message_confirm_delete_img_title = "Delete image"
            self.message_ok_delete = "The image was deleted successfully."
            self.message_ok_delete_title = "Image deleted"
            # Rename image
            self.message_rename = "Enter a new name for the image. (Only letters and numbers)."
            self.message_rename_title = "Rename image"
            self.rename_ok = "The name has been changed successfully."
            self.no_valid_name = "The name entered is not valid."

            # Recognition image
            self.message_recognition_complete_title = "Reconnaissance completed"
            self.message_recognition_complete_text = "The image was recognized correctly\nResult: {}"
            self.error_database_title = "Database error"
            self.error_database_text = "An error occurred while communicating with the database.\n" \
                                       "Result not stored.\nResult: {}"
            # Messages Backup
            self.message_confirm_backup_title = "Backup confirmation"
            self.message_confirm_backup_text = "Successful backup of results"
            self.message_error_backup_title = "Backup Failed"
            self.message_error_backup_text = "Database error\nThe system failed to back up the results." \
                                             "\n\nTry again, if the problem persists try to start the database again " \
                                             "in the settings section of the bar menu"
            self.ask_confirm_backup_title = "backup confirmation"
            self.ask_confirm_backup_text1 = "Do you want to support the current income statement?\nResults:"
            self.ask_confirm_backup_text2 = "\nThe file will be saved with the name of:\n"

            # Messages Restore
            self.ask_confirm_restore_title = "Confirmation restore"
            self.ask_confirm_restore_text = "Do you wish to continue?\nRestoring this file will lose all results " \
                                            "that were not previously backed up."
            self.Message_confirm_restore_title = "Restore Confirmation"
            self.Message_confirm_restore_text = "Restoration of results succeeded"
            self.Message_error_restore_title = "Failed to restore"
            self.Message_error_restore_text = "CORRUPT OR MISSING FILE\nThe system failed to restore the results." \
                                              "\n\nTry again, if the problem persists restore another result file, " \
                                              "or restore to initial state."
            # Messages Camera
            self.message_error_camera_title = "Error in camera module"
            self.message_error_camera_text = "Unsuccessful attempt to connect the camera"

            # Messages Data Base
            self.mes_error_connect_db_title = "Database connection error"
            self.mes_error_connect_db_text = "Failed to connect to the database"

            # Messages main Window
            self.ask_confirm_close_main_title = "Close main window"
            self.ask_confirm_close_main_text = "You are about to close the main window, do you want to continue?"

            # Warnings messages
            self.warning_date = "The start date exceeds the end date"
            self.warning_hour_inversed = "The start time exceeds the end time"
            self.warning_hour_invalid = "The format of a time is incorrect \nExample format: 13:00"
            self.warning_invalid_plate_name = "The plate format is incorrect\n Allowed characters: A-Za-z0-9_ -"
            self.warning_invalid_name = "The name format is incorrect\n Allowed characters: A-Za-z0-9_ -"

            # New rute cam
            self.error_rute_title = "Route error"
            self.error_rute_text = "Missing data to enter"

        elif num_language == 1:
            # Spanish Language
            # words and texts in the tabs
            self.results = "Resultados"
            self.gallery = "Galería"

            # words and texts in the menu bar
            self.menubar_results_label = 'Resultados'
            self.restore = 'Restaurar'
            self.backup = "Respaldar"
            self.settings = "Configuración"
            self.spanish = "Español"
            self.english = "Ingles"
            self.language = "Lenguaje"
            self.local_camera = "Camara local"
            self.ip_camera = "Ip camara"
            self.camera = "Camara"
            self.try_connect = "Intentar conectar Base de datos"
            self.restore_menu_file_label = 'Restaurar desde un archivo'
            self.restore_menu_initiate_label = 'Restaurar a estado inicial'

            # words camera ip
            self.protocol = "Protocolo"
            self.user = "Usuario"
            self.password = "Contraseña"
            self.ip = "Ip"
            self.port = "Puerto"
            self.ext = "Extras"
            self.protection = "Protegido"
            self.confirm = "Confirmar"
            self.cancel = "Cancelar"

            # word and texts in the galery window
            self.open = "Abrir"
            self.delete = "Eliminar"
            self.rename = "Renombrar"
            self.recognize = "Reconocer"
            self.internals = "Internas"
            self.externals = "Externas"

            # words and texts in the result window
            self.result = "Resultado"
            self.filters_title = "Filtros de búsqueda"
            self.date = "Fecha"
            self.hour = "Hora"
            self.begin = "Inicio"
            self.end = "Fin"
            self.name = "Nombre"
            self.name_image = "Nombre de la imagen"
            self.num_results = "Núm. resultados"
            self.plate = "Placa"
            self.plate_results = "(Resultados del análisis)"

            # words ant texts in the camara module
            self.title_camera = "Cámara"

            # Messages Alerts
            self.message_error_img_location = "La imagen ya no se encuentra en la ubicación, el sistema va a refrescar" \
                                              " la galería."
            self.message_error_img_location_title = "Error: ubicación de la imagen"
            # Delete image
            self.message_confirm_delete_img = "¿Desea eliminar la imagen: {}?"
            self.message_confirm_delete_img_title = "Eliminar imagen"
            self.message_ok_delete = "La imagen se eliminó correctamente."
            self.message_ok_delete_title = "Imagen eliminada"
            # Rename image
            self.message_rename = "Introduce un nuevo nombre para la imagen. (Solo letras y números)."
            self.message_rename_title = "Renombrar imagen"
            self.rename_ok = "El nombre se ha cambiado correctamente."
            self.no_valid_name = "El nombre ingresado no es válido."

            # Recognition image
            self.message_recognition_complete_title = "Reconocimiento completo"
            self.message_recognition_complete_text = "La imagen se reconoció correctamente\nResultado: {}"
            self.error_database_title = "Error con base de datos"
            self.error_database_text = "Ocurrió un error al comunicarse con la base de datos.\n" \
                                       "Resultado no almacenado.\nResultado: {}"

            # Messages Backup
            self.message_confirm_backup_title = "Confirmación de respaldo"
            self.message_confirm_backup_text = "Se ha realizado correctamente \nel respaldo de resultados"
            self.message_error_backup_title = "Error al realizar respaldo"
            self.message_error_backup_text = "Error en la base de datos\nEl sistema no logró realizar el " \
                                             "respaldo de los resultados.\n\nVuelva intentar, si el problema persiste " \
                                             "intente iniciar la base de datos nuevamente\n " \
                                             "en el apartado de ajustes del menú bar"
            self.ask_confirm_backup_title = "Confirmación respaldar"
            self.ask_confirm_backup_text1 = "¿Desea respaldar el estado actual de resultados?\nResutlados:"
            self.ask_confirm_backup_text2 = "\nEl archivo será guardado bajo el nombre de: \n"

            # Messages Restore
            self.ask_confirm_restore_title = "Confirmación restaurar"
            self.ask_confirm_restore_text = "¿Desea continuar?\nAl restaurar este archivo se perderán todos los\n" \
                                            "resultados que no hayan sido respaldados\ncon anterioridad"
            self.Message_confirm_restore_title = "Confirmación de restauración"
            self.Message_confirm_restore_text = "Se ha realizado correctamente la\nrestauración de resultados"
            self.Message_error_restore_title = "Error al restaurar"
            self.Message_error_restore_text = "ARCHIVO CORRUPTO O INEXISTENTE\nEl sistema no logro realizar la " \
                                              "restauración de los\nresultados.\n\nVuelva intentar, si el problema " \
                                              "persiste restaure otro\n archivo de resultados, o restaure a estado inicial."

            # Messages Camera
            self.message_error_camera_title = "Error en módulo de cámara"
            self.message_error_camera_text = "Fallo en la conexión con la cámara"

            # Messages Data Base
            self.mes_error_connect_db_title = "Fallo conexión BD"
            self.mes_error_connect_db_text = "Fallo en la conexión con la base de datos"

            # Messages main Window
            self.ask_confirm_close_main_title = "Cerrar ventana principal"
            self.ask_confirm_close_main_text = "Esta por cerrar la ventana principal, ¿desea continuar?"

            # Warnings messages
            self.warning_date = "La fecha de inicio supera la fecha de fin"
            self.warning_hour_inversed = "La hora de inicio supera la hora de fin"
            self.warning_hour_invalid = "El formato de una hora es incorrecto\n Formato ejemplo: 13:00 "
            self.warning_invalid_plate_name = "El formato de la placa es incorrecto\n Caracteres permitidos: A-Za-z0-9_ -"
            self.warning_invalid_name = "El formato de nombre es incorrecto\n Caracteres permitidos: A-Za-z0-9_ -"

            # New rute cam
            self.error_rute_title = "Error en la ruta"
            self.error_rute_text = "Faltan datos por ingresar "
