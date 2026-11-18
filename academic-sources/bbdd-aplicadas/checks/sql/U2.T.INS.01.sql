-- u2 · Instalación: memoria máxima del motor (por defecto no hay tope práctico).
SELECT name AS Opcion, value_in_use AS ValorEnUso
FROM sys.configurations
WHERE name = N'max server memory (MB)';
