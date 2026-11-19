import json
import os
import qrcode


def crear_registro_mascota(datos, url_base):
    id_mascota = datos["id"]

    # 1. Asegurar que existan los directorios
    os.makedirs("fichas", exist_ok=True)
    os.makedirs("qrs_grabado", exist_ok=True)

    # 2. Guardar el JSON individual de la mascota
    ruta_json = os.path.join("fichas", f"{id_mascota}.json")
    with open(ruta_json, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    # 3. Generar QR apuntando al HTML maestro con el parámetro ?id=
    url_final = f"{url_base.rstrip('/')}/?id={id_mascota}"

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Soporta desgaste del grabado
        box_size=10,
        border=4,
    )
    qr.add_data(url_final)
    qr.make(fit=True)

    ruta_qr = os.path.join("qrs_grabado", f"qr_{id_mascota}.png")
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(ruta_qr)

    print(f"✅ JSON creado: {ruta_json}")
    print(f"✅ QR para láser guardado: {ruta_qr}")
    print(f"🔗 URL de destino: {url_final}")


# --- EJEMPLO DE USO ---
# Cambia esta URL por la de tu repositorio en GitHub Pages o dominio propio
URL_SITIO = "https://emmcabrera.github.io/dartha_pet"

mascota_nueva = {
    "id": "honey-001",
    "nombre": "Honey Bella",
    "especie": "Perro",
    "raza": "Coquer spaniel",
    "edad": "2 años",
    "microchip": "981000012345678",
    "salud_notas": "Esterilizada. Toma medicación renal. Muy asustadiza.",
    "dueno": "Carlos Mendoza",
    "telefono": "527441794526",
    "direccion": "cuajimalpa, CDMX",
    "foto_url": ""
}

if __name__ == "__main__":
    crear_registro_mascota(mascota_nueva, URL_SITIO)