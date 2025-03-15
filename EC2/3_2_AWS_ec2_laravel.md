# Deploy Laravel en AWS EC2 con Amazon Linux 2023 y Apache

Esta guía explica cómo desplegar Laravel en una instancia EC2 con **Amazon Linux 2023** y **Apache**.

## Solución a errores comunes

### 1. `amazon-linux-extras: command not found`
En Amazon Linux 2023, el comando `amazon-linux-extras` ya no está disponible. En su lugar, usa `dnf` para instalar PHP y MySQL:
```bash
sudo dnf install -y php-cli php-mbstring php-xml php-curl php-zip php-pdo php-fpm php-mysqlnd unzip
```

### 2. `Unable to find a match: php-mysql`
El paquete correcto en Amazon Linux 2023 es `php-mysqlnd`, no `php-mysql`.
```bash
sudo dnf install -y php-mysqlnd
```

### 3. `apt: command not found`
`apt` solo funciona en Ubuntu/Debian. En Amazon Linux 2023, usa `dnf` o `yum`.
```bash
sudo dnf update -y
```

---

## 4. Actualizar paquetes
```bash
sudo dnf update -y
```

## 5. Instalar Apache
```bash
sudo dnf install -y httpd
```

## 6. Habilitar y arrancar Apache
```bash
sudo systemctl enable --now httpd
```

## 7. Verificar que Apache está corriendo
```bash
sudo systemctl status httpd
```


## 8. Configurar Apache para Laravel
Edita el archivo de configuración de Apache:
```bash
sudo vi /etc/httpd/conf.d/laravel.conf
```

Añade el siguiente contenido:
```apache
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot "/var/www/laravel/public"
    <Directory "/var/www/laravel/public">
        AllowOverride All
        Require all granted
    </Directory>
    ErrorLog "/var/log/httpd/laravel-error.log"
    CustomLog "/var/log/httpd/laravel-access.log" common
</VirtualHost>
```

## 8. Aplica los cambios:
```bash
sudo systemctl restart httpd
```

## 9. Instalar Laravel

### 10 Descargar Composer
```bash
curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer
```

### 11 Crear un Proyecto Laravel
Ubícate en la carpeta donde deseas crear el proyecto (por ejemplo, en `/var/www`):
```bash
cd /var/www
sudo composer create-project --prefer-dist laravel/laravel laravel
```

### 12 Configurar Permisos
Laravel necesita permisos adecuados en las carpetas `storage` y `bootstrap/cache`:
```bash
sudo chown -R apache:apache /var/www/laravel
sudo chmod -R 775 /var/www/laravel/storage /var/www/laravel/bootstrap/cache
```

## 13 Acceder a Laravel
Abre en tu navegador:
🔗 `http://tu-ip-publica`

¡Tu aplicación Laravel ya está funcionando en **Amazon Linux 2023 con Apache**! 🚀🎉

openssl 
mod_ssl

