
# 🎬 Proyecto Final: Plataforma de Streaming tipo Netflix

Este proyecto simula una plataforma de streaming en Python utilizando buenas prácticas, patrones de diseño y conexión a base de datos.

---

## 📁 Estructura del Proyecto

```
├── main.py
├── models/               # Entidades: Usuario, Contenido, Película, Serie
├── services/             # Lógica de negocio (registro, visualización, autenticación)
├── factories/            # Fábricas para instanciar objetos
├── repositories/         # Acceso a datos (DAO)
├── db/                   # Conexión a la base de datos
├── data/                 # Datos CSV y JSON
├── utils/                # Funciones auxiliares y validadores
├── tests/                # Pruebas unitarias
```

---

## 🔧 Funcionalidades

- Registro y autenticación de usuarios
- Gestión de películas y series
- Historial de visualizaciones
- Acceso a datos en SQL Server
- Patrón Factory para crear entidades
- Patrón Repository para acceso a datos
- Buenas prácticas: SRP, DRY, tipado, validaciones

---

## 🧪 Ejecución de pruebas

Instala `pytest` y ejecuta:

```bash
pip install pytest
pytest tests/
```

---

## 🧠 Patrones de Diseño Aplicados

- Factory
- Service Layer
- Repository

---

## ✅ Requisitos

```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

```bash
python main.py
```

---
