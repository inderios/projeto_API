# nginx/Dockerfile

# Use a imagem oficial do Nginx
FROM nginx:stable-alpine

# Remova a configuração padrão do Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copie a nossa configuração customizada para o lugar correto
COPY nginx.conf /etc/nginx/conf.d/