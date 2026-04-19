# 🧠 HealthTech RAG Project

Sistema inteligente de consulta interna basado en inteligencia artificial utilizando la técnica **RAG (Retrieval-Augmented Generation)**.

---

## 📌 Descripción

Este proyecto implementa una solución que permite consultar información interna de una organización mediante lenguaje natural.

El sistema combina:

* Recuperación de información desde documentos (PDF)
* Generación de respuestas con un modelo de lenguaje (LLM)

Esto permite obtener respuestas precisas basadas en datos reales, mejorando el acceso a la información y la eficiencia operativa.

---

## 🏢 Caso de uso

La solución está diseñada para la empresa **HealthTech Innovations**, la cual presenta dificultades en el acceso a la información interna, generando:

* Retrasos en proyectos
* Duplicación de tareas
* Errores en la toma de decisiones

El sistema permite centralizar el conocimiento y responder consultas de forma rápida y eficiente.

---

## ⚙️ Tecnologías utilizadas

* Python
* FastAPI
* LangChain
* FAISS (base de datos vectorial)
* Sentence Transformers (embeddings locales)
* GitHub Models (LLM)

---

## 🧠 ¿Qué es RAG?

RAG (Retrieval-Augmented Generation) es una técnica que combina:

1. Recuperación de información relevante desde documentos
2. Generación de respuestas mediante modelos de lenguaje

Esto permite responder preguntas utilizando datos reales en lugar de información genérica.

---

## 🔄 Flujo del sistema

1. El usuario realiza una consulta
2. El sistema busca información relevante en los documentos
3. Se construye un contexto con los datos encontrados
4. El modelo de lenguaje genera una respuesta
5. Se entrega la respuesta al usuario

---

## 🏗️ Arquitectura

Usuario → API (FastAPI) → Backend → RAG → Base Vectorial (FAISS) → LLM → Respuesta

---

## 🚀 Instalación y ejecución

### 1. Clonar repositorio

```bash
git clone <url-del-repo>
cd HealthTech-RAG-Project
```

---

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 3. Configurar variables de entorno

Crear archivo `.env`:

```env
GITHUB_TOKEN=tu_token
GITHUB_BASE_URL=https://models.inference.ai.azure.com
```

---

### 4. Ejecutar el servidor

```bash
python -m uvicorn main:app --reload
```

---

## 🌐 Uso

Abrir en el navegador:

```
http://127.0.0.1:8000/preguntar?pregunta=¿Cuál es el problema de la empresa?
```

También puedes usar la interfaz interactiva:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Ejemplos de consultas

* ¿Cuál es el problema de la empresa?
* ¿Qué solución se propone?
* ¿Qué es RAG?
* ¿Cómo funciona el sistema?
* ¿Cuáles son los beneficios?

---

## ⚠️ Limitaciones

* El sistema responde únicamente con información disponible en los documentos
* No responde preguntas fuera del contexto
* Depende de la calidad y actualización de los datos

---

## 🔐 Seguridad

El sistema considera buenas prácticas como:

* Protección de datos
* Control de acceso
* Cumplimiento de normativas como la Ley 19.628

---

## 📈 Mejoras futuras

* Integración con sistemas internos
* Soporte para múltiples documentos
* Interfaz tipo chat
* Uso de modelos más avanzados

---

## 👥 Autores

* Martin Andres Diaz Gonzalez
* Diego Andres Diaz Hernandez
* Michelle Alejandra Farias Diaz

---

## 📚 Conclusión

Este proyecto demuestra cómo la combinación de inteligencia artificial y recuperación de información permite mejorar el acceso a datos dentro de una organización, reduciendo errores y aumentando la eficiencia operativa.

---
