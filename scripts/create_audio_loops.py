#!/usr/bin/env python3
"""
Script para crear loops de audio con duracion exacta
Parte del proyecto Resonant Bonds

Requiere: ffmpeg instalado y en PATH
Instalar: https://www.ffmpeg.org/download.html
"""

import subprocess
from pathlib import Path
import json


def get_audio_duration(audio_path):
    """
    Obtiene la duracion de un archivo de audio en segundos usando ffprobe
    """
    try:
        cmd = [
            'ffprobe',
            '-v', 'error',
            '-show_entries', 'format=duration',
            '-of', 'json',
            str(audio_path)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        duration = float(data['format']['duration'])
        return duration
    except Exception as e:
        print(f"[ERROR] No se pudo obtener duracion de {audio_path}: {e}")
        return None


def calculate_loop_count(track_duration, target_duration=300):
    """
    Calcula cuantas veces repetir el track para alcanzar exactamente
    o superar ligeramente la duracion objetivo (default: 5 min = 300 seg)

    Returns: (loop_count, final_duration)
    """
    import math
    loop_count = math.ceil(target_duration / track_duration)
    final_duration = loop_count * track_duration
    return loop_count, final_duration


def create_audio_loop(input_path, output_path, target_duration=300):
    """
    Crea un loop de audio que dure exactamente el numero de repeticiones
    necesarias para alcanzar o superar la duracion objetivo

    Args:
        input_path: Ruta al audio original
        output_path: Ruta donde guardar el loop
        target_duration: Duracion objetivo en segundos (default: 300 = 5 min)
    """
    print(f"Procesando: {input_path.name}")

    # Obtener duracion del track
    track_duration = get_audio_duration(input_path)
    if not track_duration:
        return False

    print(f"  Duracion original: {track_duration:.2f} segundos")

    # Calcular repeticiones
    loop_count, final_duration = calculate_loop_count(track_duration, target_duration)
    print(f"  Repeticiones: {loop_count}x")
    print(f"  Duracion final: {final_duration:.2f} segundos ({final_duration/60:.2f} min)")

    # Crear loop usando stream_loop de ffmpeg
    # -stream_loop N repite el input N+1 veces (por eso usamos loop_count-1)
    cmd = [
        'ffmpeg',
        '-stream_loop', str(loop_count - 1),
        '-i', str(input_path),
        '-c', 'copy',  # Copia sin recodificar
        '-y',  # Sobrescribir si existe
        str(output_path)
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"  [OK] Creado: {output_path.name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR] Fallo al crear loop: {e}")
        return False


def main():
    # Definir directorios
    project_root = Path(__file__).parent.parent
    audio_dir = project_root / "audio"
    output_dir = project_root / "audio" / "loops"

    # Crear directorio de salida
    output_dir.mkdir(exist_ok=True, parents=True)

    print("=" * 60)
    print("Creacion de Audio Loops (5 minutos)")
    print("Proyecto: Resonant Bonds")
    print("=" * 60)
    print()

    # Buscar archivos de audio WAV o MP3
    audio_files = list(audio_dir.glob("*.wav")) + list(audio_dir.glob("*.mp3"))
    audio_files = [f for f in audio_files if f.is_file()]

    if not audio_files:
        print("[WARNING] No se encontraron archivos de audio en audio/")
        print("Coloca tus archivos WAV o MP3 en la carpeta 'audio/'")
        return

    print(f"Encontrados {len(audio_files)} archivos de audio")
    print()

    success_count = 0

    for audio_file in audio_files:
        # Crear nombre de salida
        output_name = f"{audio_file.stem}_loop{audio_file.suffix}"
        output_path = output_dir / output_name

        # Crear loop (5 minutos = 300 segundos)
        if create_audio_loop(audio_file, output_path, target_duration=300):
            success_count += 1
        print()

    print("=" * 60)
    print(f"Loops creados: {success_count}/{len(audio_files)}")
    print(f"Ubicacion: {output_dir}")
    print("=" * 60)


if __name__ == "__main__":
    # Verificar que ffmpeg este instalado
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("[ERROR] FFmpeg no esta instalado o no esta en PATH")
        print("Descarga e instala FFmpeg desde: https://www.ffmpeg.org/download.html")
        print()
        print("En Windows:")
        print("1. Descarga FFmpeg desde https://github.com/BtbN/FFmpeg-Builds/releases")
        print("2. Extrae el archivo ZIP")
        print("3. Agrega la carpeta 'bin' al PATH de Windows")
        exit(1)

    main()
