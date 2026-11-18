-- u1 · repaso: CHECK, DEFAULT, UNIQUE y NOT NULL con restricciones nombradas.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Vehiculo (
    VehiculoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Vehiculo PRIMARY KEY,
    Patente    CHAR(7)     NOT NULL,
    Anio       INT         NOT NULL CONSTRAINT CK_Vehiculo_Anio CHECK (Anio > 1900),
    Estado     VARCHAR(10) NOT NULL CONSTRAINT DF_Vehiculo_Estado DEFAULT ('activo'),
    CONSTRAINT UQ_Vehiculo_Patente UNIQUE (Patente),
    CONSTRAINT CK_Vehiculo_Patente CHECK (
        Patente LIKE '[A-Z][A-Z][0-9][0-9][0-9][A-Z][A-Z]'   -- formato Mercosur
        OR Patente LIKE '[A-Z][A-Z][A-Z][0-9][0-9][0-9]'      -- formato anterior
    )
);

INSERT INTO academia.Vehiculo (Patente, Anio) VALUES ('AB123CD', 2020), ('ABC123', 2010);

DECLARE @ErrorPatente INT = 0, @ErrorAnio INT = 0, @ErrorDuplicada INT = 0;
BEGIN TRY INSERT INTO academia.Vehiculo (Patente, Anio) VALUES ('1234567', 2020); END TRY
BEGIN CATCH SET @ErrorPatente = ERROR_NUMBER(); END CATCH;
BEGIN TRY INSERT INTO academia.Vehiculo (Patente, Anio) VALUES ('ZZ999YY', 1800); END TRY
BEGIN CATCH SET @ErrorAnio = ERROR_NUMBER(); END CATCH;
BEGIN TRY INSERT INTO academia.Vehiculo (Patente, Anio) VALUES ('AB123CD', 2021); END TRY
BEGIN CATCH SET @ErrorDuplicada = ERROR_NUMBER(); END CATCH;

SELECT
    (SELECT COUNT(*) FROM academia.Vehiculo)                           AS Filas,
    (SELECT MIN(Estado) FROM academia.Vehiculo)                        AS EstadoPorDefecto,
    @ErrorPatente AS ErrorPatente, @ErrorAnio AS ErrorAnio, @ErrorDuplicada AS ErrorDuplicada;
