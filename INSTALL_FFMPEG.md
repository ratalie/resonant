# Guía de Instalación - FFmpeg en Windows

FFmpeg es necesario para ejecutar los scripts de automatización de audio y video.

## Opción 1: Instalación rápida con Chocolatey (Recomendado)

Si tienes Chocolatey instalado:

```powershell
choco install ffmpeg
```

## Opción 2: Instalación manual

### Paso 1: Descargar FFmpeg

1. Ve a: https://github.com/BtbN/FFmpeg-Builds/releases
2. Descarga el archivo más reciente que diga:
   - `ffmpeg-master-latest-win64-gpl.zip`

### Paso 2: Extraer archivos

1. Extrae el archivo ZIP en una ubicación permanente, por ejemplo:
   - `C:\ffmpeg\`
2. Dentro encontrarás una carpeta como `ffmpeg-master-latest-win64-gpl`
3. Dentro de esa carpeta hay una subcarpeta llamada `bin`

### Paso 3: Agregar FFmpeg al PATH

#### Método A: Usando PowerShell (Rápido)

Abre PowerShell como **Administrador** y ejecuta:

```powershell
# Cambia esta ruta si extrajiste FFmpeg en otra ubicación
$ffmpegPath = "C:\ffmpeg\ffmpeg-master-latest-win64-gpl\bin"

# Agregar al PATH del usuario
[Environment]::SetEnvironmentVariable(
    "Path",
    [Environment]::GetEnvironmentVariable("Path", "User") + ";$ffmpegPath",
    "User"
)

Write-Host "FFmpeg agregado al PATH. Cierra y reabre tu terminal."
```

#### Método B: Usando la interfaz gráfica

1. Presiona `Win + R` y escribe: `sysdm.cpl`
2. Ve a la pestaña **"Opciones avanzadas"**
3. Haz clic en **"Variables de entorno"**
4. En **"Variables de usuario"**, selecciona **Path** y haz clic en **"Editar"**
5. Haz clic en **"Nuevo"** y agrega la ruta completa a la carpeta `bin`, ejemplo:
   ```
   C:\ffmpeg\ffmpeg-master-latest-win64-gpl\bin
   ```
6. Haz clic en **"Aceptar"** en todas las ventanas

### Paso 4: Verificar la instalación

1. **Cierra y reabre** tu terminal o Visual Studio Code
2. Ejecuta:

```bash
ffmpeg -version
```

Si ves información sobre la versión de FFmpeg, ¡la instalación fue exitosa!

## Probar los scripts

Una vez que FFmpeg esté instalado, puedes ejecutar:

### 1. Crear loops de audio (5 minutos)

```bash
cd resonant
python scripts/create_audio_loops.py
```

**Nota**: Primero necesitas tener archivos de audio WAV o MP3 en la carpeta `audio/`

### 2. Crear videos (audio + visual)

```bash
python scripts/create_videos.py
```

Este script combina tus archivos de audio looped con el `source video.mp4`

## Solución de problemas

### Error: "ffmpeg: command not found"

- Asegúrate de haber cerrado y reabierto tu terminal después de agregar FFmpeg al PATH
- Verifica que la ruta agregada al PATH sea correcta y apunte a la carpeta `bin`

### Error: "No module named 'xxx'"

Si faltan módulos de Python, instálalos:

```bash
pip install --upgrade pip
```

Todos los scripts usan solo librerías estándar de Python, no necesitas instalar nada adicional.

## Recursos adicionales

- Documentación oficial de FFmpeg: https://ffmpeg.org/documentation.html
- FFmpeg para Windows: https://www.gyan.dev/ffmpeg/builds/
