# To-Do-List-API
API для списка дел(задач)
## Основной функционал
### Пользователи
**Возможности:**
1. Идентификация и аутентификация по JWT-токену (вход по никнейму или почте)
2. Подтверждение email

### Задачи
Задачи (или Task) может создавать любой зарегистрированный пользователь.

**Особенности:**

Пользователь видит и взаимодействует только со своими задачами

**Возможности:**
1. Просмотр пользователем всех своих Задач
2. Фильтрация задач по статусу, времени создания и дедлайну
3. Поиск задач по названию
4. Упорядочивание по имени, времени создания и дедлайну
5. Создание новой задачи
6. Изменение (статуса, описания, названия и дедлайна), Просмотр и Удаление отдельной задачи
