-- u1 · repaso: DDL trigger que impide DROP TABLE.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (AlumnoId INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY);
GO
CREATE TRIGGER TrgNoDropTable
ON DATABASE
FOR DROP_TABLE
AS
BEGIN
    PRINT 'No se permite eliminar tablas.';
    ROLLBACK;
END;
GO
DECLARE @Error INT = 0;
BEGIN TRY
    DROP TABLE academia.Alumno;
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT
    @Error AS Error,
    CASE WHEN OBJECT_ID('academia.Alumno') IS NOT NULL THEN 'existe' ELSE 'eliminada' END AS Tabla;
GO
DROP TRIGGER TrgNoDropTable ON DATABASE;
