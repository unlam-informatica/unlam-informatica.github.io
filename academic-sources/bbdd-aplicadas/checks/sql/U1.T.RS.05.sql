-- u1 · repaso: acciones referenciales NO ACTION, CASCADE, SET NULL y SET DEFAULT.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Categoria (
    CategoriaId INT NOT NULL CONSTRAINT PK_Categoria PRIMARY KEY,
    Nombre      VARCHAR(30) NOT NULL
);

CREATE TABLE academia.ArticuloNoAction (
    ArticuloId  INT NOT NULL PRIMARY KEY,
    CategoriaId INT NOT NULL
        CONSTRAINT FK_ArticuloNoAction_Categoria REFERENCES academia.Categoria (CategoriaId) ON DELETE NO ACTION
);
CREATE TABLE academia.ArticuloCascade (
    ArticuloId  INT NOT NULL PRIMARY KEY,
    CategoriaId INT NOT NULL
        CONSTRAINT FK_ArticuloCascade_Categoria REFERENCES academia.Categoria (CategoriaId) ON DELETE CASCADE
);
CREATE TABLE academia.ArticuloSetNull (
    ArticuloId  INT NOT NULL PRIMARY KEY,
    CategoriaId INT NULL
        CONSTRAINT FK_ArticuloSetNull_Categoria REFERENCES academia.Categoria (CategoriaId) ON DELETE SET NULL
);
CREATE TABLE academia.ArticuloSetDefault (
    ArticuloId  INT NOT NULL PRIMARY KEY,
    CategoriaId INT NOT NULL CONSTRAINT DF_ArticuloSetDefault_Categoria DEFAULT (9)
        CONSTRAINT FK_ArticuloSetDefault_Categoria REFERENCES academia.Categoria (CategoriaId) ON DELETE SET DEFAULT
);

INSERT INTO academia.Categoria (CategoriaId, Nombre)
VALUES (1, 'Libros'), (2, 'Cuadernos'), (3, 'Lapices'), (4, 'Mochilas'), (9, 'Sin clasificar');
INSERT INTO academia.ArticuloNoAction  VALUES (1, 1);
INSERT INTO academia.ArticuloCascade   VALUES (1, 2);
INSERT INTO academia.ArticuloSetNull   VALUES (1, 3);
INSERT INTO academia.ArticuloSetDefault VALUES (1, 4);

DECLARE @ErrorNoAction INT = 0;
BEGIN TRY
    DELETE FROM academia.Categoria WHERE CategoriaId = 1;
END TRY
BEGIN CATCH
    SET @ErrorNoAction = ERROR_NUMBER();
END CATCH;
DELETE FROM academia.Categoria WHERE CategoriaId IN (2, 3, 4);

SELECT 'NO ACTION' AS Accion,
       CAST(@ErrorNoAction AS VARCHAR(10)) AS Resultado
UNION ALL
SELECT 'CASCADE',     CAST(COUNT(*) AS VARCHAR(10)) + ' filas hijas' FROM academia.ArticuloCascade
UNION ALL
SELECT 'SET NULL',    ISNULL(CAST(CategoriaId AS VARCHAR(10)), 'NULL') FROM academia.ArticuloSetNull
UNION ALL
SELECT 'SET DEFAULT', CAST(CategoriaId AS VARCHAR(10)) FROM academia.ArticuloSetDefault;
