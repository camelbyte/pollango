# Django Management Commands

This table lists some useful Django management commands and their descriptions.

| Command                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `cleanup`                | Remove old data from the database.                                           |
| `compilemessages`        | Compile `.po` files to `.mo` for use with gettext.                           |
| `createcachetable`       | Creates table for SQL cache backend.                                         |
| `createsuperuser`        | Create a superuser.                                                          |
| `dbshell`                | Run command-line client for the current database.                            |
| `diffsettings`           | Display differences between the current settings and Django's default.      |
| `dumpdata`               | Output contents of the database as a fixture.                                |
| `flush`                  | Execute `sqlflush` on the current database.                                  |
| `inspectdb`              | Output Django model module for tables in the database.                       |
| `loaddata`               | Install the named fixture(s) in the database.                               |
| `makemessages`           | Pull out all strings marked for translation.                                 |
| `reset`                  | Executes `sqlreset` for the given app(s).                                    |
| `runfcgi`                | Run this project as a FastCGI application.                                   |
| `runserver`              | Start a lightweight web server for development.                              |
| `shell`                  | Run a Python interactive interpreter. Tries to use IPython if available.   |
| `sqlall`                 | Print the `CREATE TABLE`, `CREATE INDEX`, and custom SQL statements.        |
| `sqlclear`               | Print the `DROP TABLE` statements for the given app(s).                     |
| `sqlcustom`              | Print the custom table-modifying SQL statements for the given app(s).       |
| `sqlflush`               | Print the SQL statements required to return all tables to initial state.   |
| `sqlindexes`             | Print the `CREATE INDEX` statements for the given app(s).                   |
| `sql`                    | Print the `CREATE TABLE` statements for the given app(s).                   |
| `sqlreset`               | Print the `DROP TABLE` and `CREATE TABLE` statements for the given app(s).  |
| `sqlsequencereset`       | Print the SQL statements for resetting sequences for the given app(s).     |
| `startapp`               | Create a Django app directory in this project's directory.                  |
| `startproject`           | Create a Django project directory structure for a given project.            |
| `syncdb`                 | Create database tables for apps in `INSTALLED_APPS` that require them.      |
| `test`                   | Run the test suite for the specified app, or the entire site.               |
| `testserver`             | Run a development server with data from the given fixture(s).               |
| `validate`               | Validate all installed modules.                                             |
