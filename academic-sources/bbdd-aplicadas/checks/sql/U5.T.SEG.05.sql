-- SIN-PRELUDE
-- Permisos efectivos de un usuario que pertenece a dos roles.
CREATE SCHEMA ventas;
GO
CREATE SCHEMA compras;
GO
CREATE TABLE ventas.Pedido (PedidoId INT PRIMARY KEY, Importe DECIMAL(10, 2) NOT NULL);
CREATE TABLE compras.Proveedor (ProveedorId INT PRIMARY KEY, Nombre VARCHAR(50) NOT NULL);
CREATE ROLE rol_ventas;
CREATE ROLE rol_auditoria;
CREATE USER usr_ana WITHOUT LOGIN;
ALTER ROLE rol_ventas ADD MEMBER usr_ana;
ALTER ROLE rol_auditoria ADD MEMBER usr_ana;
GRANT SELECT, INSERT, DELETE ON OBJECT::ventas.Pedido TO rol_ventas;
GRANT SELECT ON SCHEMA::compras TO rol_auditoria;
DENY DELETE ON OBJECT::ventas.Pedido TO rol_auditoria;
GO
EXECUTE AS USER = 'usr_ana';
SELECT entity_name, subentity_name, permission_name
FROM fn_my_permissions('ventas.Pedido', 'OBJECT')
ORDER BY permission_name, subentity_name;
SELECT HAS_PERMS_BY_NAME('ventas.Pedido', 'OBJECT', 'SELECT') AS PuedeSelect,
       HAS_PERMS_BY_NAME('ventas.Pedido', 'OBJECT', 'DELETE') AS PuedeDelete,
       HAS_PERMS_BY_NAME('compras.Proveedor', 'OBJECT', 'SELECT') AS PuedeLeerProveedor;
REVERT;
GO
SELECT rol.name AS Rol, miembro.name AS Miembro
FROM sys.database_role_members AS drm
JOIN sys.database_principals AS rol ON rol.principal_id = drm.role_principal_id
JOIN sys.database_principals AS miembro ON miembro.principal_id = drm.member_principal_id
WHERE miembro.name = 'usr_ana'
ORDER BY rol.name;
