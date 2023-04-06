const { createProxyMiddleware } = require('http-proxy-middleware');

const port = import.meta.env.VITE_API_PORT 
const api = import.meta.env.VITE_API_URL 
const auth = import.meta.env.VITE_AUTH_URL
const admin = import.meta.env.VITE_ADMIN_URL
const socketio = import.meta.env.VITE_SOCKETIO_URL
const url = 'http://127.0.0.1:'+port.toString()

module.exports = function(app) {
    app.use(socketio, createProxyMiddleware({ 'target': url, 'ws': true }));
    app.use(api,      createProxyMiddleware({ 'target': url })); 
    app.use(auth,     createProxyMiddleware({ 'target': url })); 
    app.use(admin,    createProxyMiddleware({ 'target': url })); 
};

