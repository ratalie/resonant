#!/usr/bin/env python3
"""
Script para convertir archivos MusicXML a MIDI
Parte del proyecto Resonant Bonds
"""

import os
from pathlib import Path

try:
    from music21 import converter
except ImportError:
    print("Error: music21 no está instalado.")
    print("Instala con: pip install music21")
    exit(1)


def convert_musicxml_to_midi(musicxml_path, output_dir):
    """
    Convierte un archivo MusicXML a MIDI

    Args:
        musicxml_path: Ruta al archivo MusicXML
        output_dir: Directorio donde guardar el MIDI
    """
    try:
        print(f"Convirtiendo: {musicxml_path}")

        # Cargar el archivo MusicXML
        score = converter.parse(musicxml_path)

        # Crear nombre de salida
        input_name = Path(musicxml_path).stem
        output_path = Path(output_dir) / f"{input_name}.mid"

        # Exportar a MIDI
        score.write('midi', fp=str(output_path))

        print(f"[OK] Creado: {output_path}")
        return True

    except Exception as e:
        print(f"[ERROR] Error al convertir {musicxml_path}: {e}")
        return False


def main():
    # Definir directorios
    project_root = Path(__file__).parent.parent
    scores_dir = project_root / "scores"
    midi_dir = project_root / "midi"

    # Crear directorio de salida si no existe
    midi_dir.mkdir(exist_ok=True)

    # Lista de archivos a convertir
    musicxml_files = [
        "N_Healing_Containment_Track2.musicxml",
        "N_Healing_Balance_Track3.musicxml",
        "N_Healing_Depth_Track4.musicxml",
        "N_Healing_Activation_Track5.musicxml"
    ]

    print("=" * 50)
    print("Conversion MusicXML -> MIDI")
    print("Proyecto: Resonant Bonds")
    print("=" * 50)
    print()

    success_count = 0
    total_count = len(musicxml_files)

    for filename in musicxml_files:
        musicxml_path = scores_dir / filename

        if not musicxml_path.exists():
            print(f"[WARNING] Archivo no encontrado: {filename}")
            continue

        if convert_musicxml_to_midi(musicxml_path, midi_dir):
            success_count += 1
        print()

    print("=" * 50)
    print(f"Conversion completada: {success_count}/{total_count}")
    print("=" * 50)


if __name__ == "__main__":
    main()
