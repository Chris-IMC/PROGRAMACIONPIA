#MODIFICAR $RUTACARPETA Y RUTA DE ARCHIVO EXCEL DE SALIDA.
# Ruta de la carpeta con las imágenes
$rutaCarpeta = "C:\Python\PROGRAMACIONPIA\Imagenes"

# Ruta y nombre del archivo Excel de salida
$rutaArchivoExcel = "C:\Python\PROGRAMACIONPIA\Metadatos2.xlsx"

# Cargar el ensamblado de System.Drawing y Microsoft.Office.Interop.Excel
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName Microsoft.Office.Interop.Excel

# Crear una instancia de Excel
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false

# Crear un nuevo libro de Excel
$libro = $excel.Workbooks.Add()

# Obtener la hoja activa
$hojaActiva = $libro.ActiveSheet

# Obtener la lista de archivos de imagen en la carpeta
$archivosImagen = Get-ChildItem -Path $rutaCarpeta -Filter "*.jpg" -File

# Definir los encabezados de columna en Excel
$hojaActiva.Cells.Item(1, 1) = "Archivo"
$hojaActiva.Cells.Item(1, 2) = "Ubicación"
$hojaActiva.Cells.Item(1, 3) = "Resolución Horizontal"
$hojaActiva.Cells.Item(1, 4) = "Resolución Vertical"
$hojaActiva.Cells.Item(1, 5) = "Modelo de Dispositivo"

# Iterar sobre los archivos de imagen y obtener los metadatos
$fila = 2

foreach ($archivo in $archivosImagen) {
    $rutaImagen = $archivo.FullName

    # Crear un objeto Image a partir de la imagen
    $imagen = [System.Drawing.Image]::FromFile($rutaImagen)

    # Obtener la ubicación (si está disponible)
    if ($imagen.PropertyIdList -contains 0x9286) {
        $ubicacionBytes = $imagen.GetPropertyItem(0x9286).Value
        $latitud = [BitConverter]::ToSingle($ubicacionBytes, 0)
        $longitud = [BitConverter]::ToSingle($ubicacionBytes, 4)
        $hojaActiva.Cells.Item($fila, 2) = "$latitud, $longitud"
    }

    # Obtener la resolución
    $resolucionHorizontal = $imagen.HorizontalResolution
    $resolucionVertical = $imagen.VerticalResolution
    $hojaActiva.Cells.Item($fila, 3) = $resolucionHorizontal
    $hojaActiva.Cells.Item($fila, 4) = $resolucionVertical

    # Obtener el modelo del dispositivo
    if ($imagen.PropertyIdList -contains 0x0110) {
        $modeloDispositivo = [System.Text.Encoding]::ASCII.GetString($imagen.GetPropertyItem(0x0110).Value)
        $hojaActiva.Cells.Item($fila, 5) = $modeloDispositivo
    }

    # Escribir el nombre del archivo en la columna 1
    $hojaActiva.Cells.Item($fila, 1) = $archivo.Name

    # Liberar los recursos
    $imagen.Dispose()

    $fila++
}

# Ajustar el ancho de las columnas
$hojaActiva.Columns.Item(1).AutoFit()
$hojaActiva.Columns.Item(2).AutoFit()
$hojaActiva.Columns.Item(3).AutoFit()
$hojaActiva.Columns.Item(4).AutoFit()
$hojaActiva.Columns.Item(5).AutoFit()

# Guardar el libro de Excel
$libro.SaveAs($rutaArchivoExcel)

# Cerrar el libro y la aplicación de Excel
$libro.Close($true)
$excel.Quit()

# Liberar los recursos COM
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($libro) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()

Write-Host "Los metadatos se han guardado en el archivo Excel: $rutaArchivoExcel"