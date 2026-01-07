#!/usr/bin/env python3
"""
Script para crear videos combinando audio looped + video visual looped
Parte del proyecto Resonant Bonds

Requiere: ffmpeg instalado y en PATH
"""

import subprocess
from pathlib import Path
import json


def get_duration(file_path):
    """
    Obtiene la duracion de un archivo de audio o video en segundos
    """
    try:
        cmd = [
            'ffprobe',
            '-v', 'error',
            '-show_entries', 'format=duration',
            '-of', 'json',
            str(file_path)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        duration = float(data['format']['duration'])
        return duration
    except Exception as e:
        print(f"[ERROR] No se pudo obtener duracion: {e}")
        return None


def create_video_with_audio(audio_path, video_source, output_path):
    """
    Combina un archivo de audio con un video visual, looping el video
    para que coincida con la duracion del audio

    Args:
        audio_path: Ruta al archivo de audio (idealmente el loop largo)
        video_source: Ruta al video visual de fondo
        output_path: Ruta donde guardar el video final
    """
    print(f"Creando video: {output_path.name}")

    # Obtener duraciones
    audio_duration = get_duration(audio_path)
    video_duration = get_duration(video_source)

    if not audio_duration or not video_duration:
        return False

    print(f"  Audio: {audio_duration:.2f}s ({audio_duration/60:.2f} min)")
    print(f"  Video fuente: {video_duration:.2f}s")

    # Calcular cuantas veces repetir el video
    import math
    video_loops = math.ceil(audio_duration / video_duration)
    print(f"  Video se repetira: {video_loops}x")

    # Comando FFmpeg para combinar audio + video looped
    # -stream_loop repite el video
    # -shortest termina cuando el stream mas corto (audio) termina
    cmd = [
        'ffmpeg',
        '-stream_loop', str(video_loops - 1),  # Loop del video
        '-i', str(video_source),
        '-i', str(audio_path),
        '-map', '0:v:0',  # Video del primer input
        '-map', '1:a:0',  # Audio del segundo input
        '-c:v', 'libx264',  # Codec de video H.264
        '-preset', 'medium',  # Balance calidad/velocidad
        '-crf', '23',  # Calidad (18-28, menor = mejor calidad)
        '-c:a', 'aac',  # Codec de audio AAC
        '-b:a', '192k',  # Bitrate de audio
        '-shortest',  # Terminar cuando el audio termine
        '-y',  # Sobrescribir si existe
        str(output_path)
    ]

    try:
        print(f"  Procesando... (esto puede tomar varios minutos)")
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"  [OK] Video creado: {output_path.name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR] Fallo al crear video: {e}")
        if e.stderr:
            print(f"  Detalles: {e.stderr.decode()}")
        return False


def main():
    # Definir directorios
    project_root = Path(__file__).parent.parent
    audio_loops_dir = project_root / "audio" / "loops"
    videos_dir = project_root / "videos"
    video_source = project_root / "source video.mp4"

    # Crear directorio de salida
    videos_dir.mkdir(exist_ok=True)

    print("=" * 60)
    print("Creacion de Videos - Audio + Visual")
    print("Proyecto: Resonant Bonds")
    print("=" * 60)
    print()

    # Verificar que exista el video fuente
    if not video_source.exists():
        print(f"[ERROR] No se encontro el video fuente: {video_source}")
        print("Asegurate de tener 'source video.mp4' en el root del proyecto")
        return

    # Buscar archivos de audio looped
    audio_files = list(audio_loops_dir.glob("*_loop.*"))

    if not audio_files:
        print(f"[WARNING] No se encontraron archivos de audio en {audio_loops_dir}")
        print("Ejecuta primero: python scripts/create_audio_loops.py")
        return

    print(f"Encontrados {len(audio_files)} archivos de audio looped")
    print(f"Video fuente: {video_source.name}")
    print()

    success_count = 0

    for audio_file in audio_files:
        # Crear nombre de salida
        # De "N_Healing_Clarity_Track1_loop.wav" a "N_Healing_Clarity_Track1.mp4"
        base_name = audio_file.stem.replace("_loop", "")
        output_name = f"{base_name}.mp4"
        output_path = videos_dir / output_name

        # Crear video
        if create_video_with_audio(audio_file, video_source, output_path):
            success_count += 1
        print()

    print("=" * 60)
    print(f"Videos creados: {success_count}/{len(audio_files)}")
    print(f"Ubicacion: {videos_dir}")
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
