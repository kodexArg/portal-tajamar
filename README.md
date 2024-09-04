# Portal Tajamar TV

## Español

### Descripción

Repositorio de inicio para **Portal Tajamar TV**. Proyecto desarrollado con **Django** para gestionar y presentar la información de la empresa.

### Tecnologías Utilizadas

- **Django**: Framework web en Python.
- **AWS Elastic Beanstalk**: Despliegue con `eb deploy`.
- **MySQL**: Base de datos.
- **Django Storages**: Manejo de archivos en S3.
- **Bulma**: CSS responsivo.
- **HTMX y Alpine.js**: Interactividad en el frontend.
- **Loguru**: Logging.

### Despliegue y Configuración

- **Entornos**: `development`, `staging`, `production`. Configurados en `.env`.
- **AWS S3**: Archivos estáticos y media.
- **Base de datos**: MySQL en RDS. Configuración en `.env`.
- **Inicialización**: 
  1. Clona el repositorio.
  2. Crea un entorno virtual.
  3. Instala las dependencias.
  4. Configura `.env`.
  5. `python manage.py migrate`.
  6. Crea un superusuario.

### Notas

- No expongas las credenciales en `.env`.
- Los entornos deben estar correctamente configurados.
- Utiliza `eb deploy` para despliegue en Elastic Beanstalk.

## English

### Description

Starting repository for **Portal Tajamar TV**. Developed with **Django** to manage and present the company’s information.

### Technologies Used

- **Django**: Python web framework.
- **AWS Elastic Beanstalk**: Deployed with `eb deploy`.
- **MySQL**: Database.
- **Django Storages**: File handling on S3.
- **Bulma**: Responsive CSS.
- **HTMX and Alpine.js**: Frontend interactivity.
- **Loguru**: Logging.

### Deployment and Configuration

- **Environments**: `development`, `staging`, `production`. Set in `.env`.
- **AWS S3**: Static and media files.
- **Database**: MySQL on RDS. Set in `.env`.
- **Initialization**:
  1. Clone the repository.
  2. Create a virtual environment.
  3. Install dependencies.
  4. Configure `.env`.
  5. `python manage.py migrate`.
  6. Create a superuser.

### Notes

- Do not expose credentials in `.env`.
- Environments must be correctly configured.
- Use `eb deploy` for Elastic Beanstalk deployment.
