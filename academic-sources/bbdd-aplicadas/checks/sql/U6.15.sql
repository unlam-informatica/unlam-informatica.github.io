CREATE SCHEMA calidad;
GO

CREATE TABLE calidad.Contacto (
    ContactoId INT IDENTITY(1, 1) NOT NULL,
    Nombre     VARCHAR(40)        NOT NULL,
    Email      VARCHAR(80)        NULL,
    Telefono   VARCHAR(20)        NULL,
    CONSTRAINT PK_Contacto PRIMARY KEY CLUSTERED (ContactoId)
);

INSERT INTO calidad.Contacto (Nombre, Email, Telefono)
VALUES
    ('Contacto A', 'a@ejemplo.test', '11-5550-0001'),
    ('Contacto B', NULL, '11-5550-0002'),
    ('Contacto C', '', NULL),
    ('Contacto D', 'd@ejemplo.test', NULL),
    ('Contacto E', '   ', '11-5550-0005'),
    ('Contacto F', 'f@ejemplo.test', '11-5550-0006'),
    ('Contacto G', NULL, NULL),
    ('Contacto H', 'h@ejemplo.test', '11-5550-0008'),
    ('Contacto I', 'i@ejemplo.test', '11-5550-0009'),
    ('Contacto J', 'j@ejemplo.test', '11-5550-0010');
GO

SELECT
    COUNT(*)                                                         AS Evaluados,
    COUNT(Email)                                                     AS EmailNoNulo,
    SUM(CASE WHEN NULLIF(LTRIM(RTRIM(Email)), '') IS NOT NULL
             THEN 1 ELSE 0 END)                                      AS EmailConValor,
    CAST(100.0 * SUM(CASE WHEN NULLIF(LTRIM(RTRIM(Email)), '') IS NOT NULL
                          THEN 1 ELSE 0 END) / COUNT(*) AS DECIMAL(5, 1)) AS PctCompletitudEmail
FROM calidad.Contacto;
