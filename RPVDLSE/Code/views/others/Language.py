class Language():
    def __init__(self):
        # Spanish Language default
        # words and texts in the tabs
        self.results = "Resultados"
        self.galery = "Galería"

        # words and texts in the menu bar
        self.menubar_results_label = 'Resultados'
        self.restore = 'Restaurar'
        self.backup = "Respaldar"
        self.settings = "Configuración"
        self.spanish = "Español"
        self.english = "Ingles"
        self.language = "Lenguage"
        self.restore_menu_file_label = 'Restaurar desde un archivo'
        self.restore_menu_initiate_label= 'Restaurar a estado inicial'
            
        # word and texts in the galery window
        self.open = "Abrir"
        self.delet = "Eliminar"
        self.rename = "Renombrar"
        self.recognize = "Reconocer"
        self.internals = "Internas"
        self.externals = "Externas"

        # words and texts in the result window
        self.result = "Resultado"
        self.filters_title = "Filtros para los resultados"
        self.date = "Fecha"
        self.hour = "Hora"
        self.begin = "Inicio"
        self.end = "Fin"
        self.name = "Nombre"
        self.name_image = "Nombre de la imagen"
        self.num_results = "Núm resultados"
        self.plate_result = "Placa\n(Resultados de el analisis)"
            
        # Messages Alerts
        # Messages Backup
        self.message_confirm_backup_title = "Confirmación de respaldo"
        self.message_confirm_backup_text = "Se ha realizado correctamente el \nrespaldo de resultados"
        self.message_error_backup_title = "Error al realizar respaldo"
        self.message_error_backup_text = "ARCHIVO CORRUPTO O INEXISTENTE\nEl sistema no logro realizar el respaldo de los resultados.\n\nVuelva intentar, si el problema persiste restaure el archivo\n resulrados, desde el menú Resultados en la barra de nenú"
        self.ask_confirm_backup_title = "Confirmación respaldar"
        self.ask_confirm_backup_text1 = "¿Desa respaldar el estado actual de resultados?\nResutlados:"
        self.ask_confirm_backup_text2 = "\nEl archivo será guardado bajo el nombre de *ResManualResultadosAAMMDD_hh-mm-ss.txt"

        # Messages Restore
        self.ask_confirm_restore_title = "Confirmación resturar"
        self.ask_confirm_restore_text = "¿Desea continuar?\nAl restaurar este archivo se perderán todos los\nresultados que no hayan sido respaldados\ncon anterioridad"
        self.Message_confirm_restore_title = "Confirmación de restauración"
        self.Message_confirm_restore_text = "Se ha realizado correctamente la\nrestauración de resultados"
        self.Message_error_restore_title = "Error al restaurar"
        self.Message_error_restore_text = "ARCHIVO CORRUPTO O INEXISTENTE\nEl sistema no logro realizar la restauración de los\nresultados.\n\nVuelva intentar, si el problema persiste restaure otro\n archivo de resultados, o restaure a estado inicial."
    
    def languageChange(self, numLenguage):
        if numLenguage == 0:
            # English Lenguage
            # words and texts in the tabs
            self.results = "Results"
            self.galery = "Galery"

            # words and texts in the menu bar
            self.menubar_results_label = 'Results'
            self.restore = 'Restore'
            self.backup = "Backup"
            self.settings = "settings"
            self.spanish = "Spanish"
            self.english = "English"
            self.language = "Language"
            self.restore_menu_file_label = 'Restaurar desde un archivo'
            self.restore_menu_initiate_label= 'Restaurar a estado inicial'
            
            # word and texts in the galery window
            self.open = "Open"
            self.delet = "Delet"
            self.rename = "Rename"
            self.recognize = "recognize"
            self.internals = "Internals"
            self.externals = "Externals"

            # words and texts in the result window
            self.result = "Result"
            self.filters_title = "Filters for the results"
            self.date = "Date"
            self.hour = "Hour"
            self.begin = "Begin"
            self.end = "End"
            self.name = "Name"
            self.name_image = "Image name"
            self.num_results = "Num of results"
            self.plate_result = "Plate\n(Analysts results)"

            # Messages Alerts
            # Messages Backup
            self.message_confirm_backup_title = "Confirmación de respaldo"
            self.message_confirm_backup_text = "Se ha realizado correctamente el \nrespaldo de resultados"
            self.message_error_backup_title = "Error al realizar respaldo"
            self.message_error_backup_text = "ARCHIVO CORRUPTO O INEXISTENTE\nEl sistema no logro realizar el respaldo de los resultados.\n\nVuelva intentar, si el problema persiste restaure el archivo\n resulrados, desde el menú Resultados en la barra de nenú"
            self.ask_confirm_backup_title = "Confirmación respaldar"
            self.ask_confirm_backup_text1 = "¿Desa respaldar el estado actual de resultados?\nResutlados:"
            self.ask_confirm_backup_text2 = "\nEl archivo será guardado bajo el nombre de *ResManualResultadosAAMMDD_hh-mm-ss.txt"

            # Messages Restore
            self.ask_confirm_restore_title = "Confirmación resturar"
            self.ask_confirm_restore_text = "¿Desea continuar?\nAl restaurar este archivo se perderán todos los\nresultados que no hayan sido respaldados\ncon anterioridad"
            self.Message_confirm_restore_title = "Confirmación de restauración"
            self.Message_confirm_restore_text = "Se ha realizado correctamente la\nrestauración de resultados"
            self.Message_error_restore_title = "Error al restaurar"
            self.Message_error_restore_text = "ARCHIVO CORRUPTO O INEXISTENTE\nEl sistema no logro realizar la restauración de los\nresultados.\n\nVuelva intentar, si el problema persiste restaure otro\n archivo de resultados, o restaure a estado inicial."
        elif numLenguage == 1:
            # Spanish Language
            # words and texts in the tabs
            self.results = "Resultados"
            self.galery = "Galería"

            # words and texts in the menu bar
            self.menubar_results_label = 'Resultados'
            self.restore = 'Restaurar'
            self.backup = "Respaldar"
            self.settings = "Configuración"
            self.spanish = "Español"
            self.english = "Ingles"
            self.language = "Lenguage"
            self.restore_menu_file_label = 'Restaurar desde un archivo'
            self.restore_menu_initiate_label= 'Restaurar a estado inicial'
            
            # word and texts in the galery window
            self.open = "Abrir"
            self.delet = "Eliminar"
            self.rename = "Renombrar"
            self.recognize = "Reconocer"
            self.internals = "Internas"
            self.externals = "Externas"

            # words and texts in the result window
            self.result = "Resultado"
            self.filters_title = "Filtros para los resultados"
            self.date = "Fecha"
            self.hour = "Hora"
            self.begin = "Inicio"
            self.end = "Fin"
            self.name = "Nombre"
            self.name_image = "Nombre de la imagen"
            self.num_results = "Núm resultados"
            self.plate_result = "Placa\n(Resultados de el analisis)"
            
            # Messages Alerts
            # Messages Backup
            self.message_confirm_backup_title = "Confirmación de respaldo"
            self.message_confirm_backup_text = "Se ha realizado correctamente el \nrespaldo de resultados"
            self.message_error_backup_title = "Error al realizar respaldo"
            self.message_error_backup_text = "ARCHIVO CORRUPTO O INEXISTENTE\nEl sistema no logro realizar el respaldo de los resultados.\n\nVuelva intentar, si el problema persiste restaure el archivo\n resulrados, desde el menú Resultados en la barra de nenú"
            self.ask_confirm_backup_title = "Confirmación respaldar"
            self.ask_confirm_backup_text1 = "¿Desa respaldar el estado actual de resultados?\nResutlados:"
            self.ask_confirm_backup_text2 = "\nEl archivo será guardado bajo el nombre de *ResManualResultadosAAMMDD_hh-mm-ss.txt"

            # Messages Restore
            self.ask_confirm_restore_title = "Confirmación resturar"
            self.ask_confirm_restore_text = "¿Desea continuar?\nAl restaurar este archivo se perderán todos los\nresultados que no hayan sido respaldados\ncon anterioridad"
            self.Message_confirm_restore_title = "Confirmación de restauración"
            self.Message_confirm_restore_text = "Se ha realizado correctamente la\nrestauración de resultados"
            self.Message_error_restore_title = "Error al restaurar"
            self.Message_error_restore_text = "ARCHIVO CORRUPTO O INEXISTENTE\nEl sistema no logro realizar la restauración de los\nresultados.\n\nVuelva intentar, si el problema persiste restaure otro\n archivo de resultados, o restaure a estado inicial."
        else:
            pass
        