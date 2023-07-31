## Ramas (Branches)

En este repositorio, utilizamos una estructura de ramas específica para gestionar el desarrollo y los entregables del equipo de Data Science. A continuación, se describen las principales ramas que utilizaremos:

### 1. `main` (rama principal)

- La rama `main` representa la versión estable y lista para producción del proyecto.
- No se deben realizar cambios directamente en esta rama.
- Los Pull Requests para cambios o correcciones deben realizarse desde otras ramas y solicitar la revisión y aprobación de al menos dos miembros del equipo antes de la fusión.

### 2. `d_engineer` (rama de ingeniería de datos)

- Esta rama se utilizará específicamente para desarrollar las tareas relacionadas con la ingeniería de datos, como la recolección, limpieza y transformación de datos.
- Todos los cambios relacionados con la ingeniería de datos deben realizarse en esta rama.
- Una vez que se complete el desarrollo, crea un Pull Request hacia `main` para revisar y fusionar los cambios.

### 3. `d_analyst` (rama de análisis de datos)

- Esta rama se utilizará específicamente para desarrollar las tareas de análisis de datos, incluida la exploración y visualización de datos.
- Todos los cambios relacionados con el análisis de datos deben realizarse en esta rama.
- Una vez que se complete el desarrollo, crea un Pull Request hacia `main` para revisar y fusionar los cambios.

### 4. `m_learning` (rama de machine learning)

- Esta rama se utilizará específicamente para desarrollar las tareas relacionadas con el machine learning, como la construcción, entrenamiento y evaluación de modelos.
- Todos los cambios relacionados con el machine learning deben realizarse en esta rama.
- Una vez que se complete el desarrollo, crea un Pull Request hacia `main` para revisar y fusionar los cambios.

### 5. `docum` (rama de documentación)

- Esta rama se utilizará específicamente para desarrollar y mantener la documentación del proyecto, incluidos informes, manuales y guías de usuario.
- Todos los cambios relacionados con la documentación deben realizarse en esta rama.
- Una vez que se complete el desarrollo, crea un Pull Request hacia `main` para revisar y fusionar los cambios.

### 6. `hotfix/nombre-del-hotfix` (ramas para correcciones rápidas)

- Las ramas `hotfix` se utilizan para correcciones críticas que deben aplicarse rápidamente a la rama `main`.
- Si surge un problema importante en la rama `main`, crea una rama `hotfix` a partir de `main`, corrige el problema y crea un Pull Request hacia `main` para su revisión y fusión.

Recuerda que estas convenciones de nombres de ramas son solo una sugerencia, y puedes adaptarlas según las necesidades específicas de tu equipo y proyecto. La clave es mantener una estructura organizada y coherente que facilite el trabajo en equipo y la colaboración eficiente.
